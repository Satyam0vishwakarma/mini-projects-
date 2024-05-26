from tkinter import *
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, window):
        window.geometry('320x180')
        window.title('Codex mini Project Player')
        window.resizable(0, 0)
        self.track_playlist = []
        self.current_track_index = None
        mixer.init()
        
        Load = Button(window, text='Load', width=10, font=('Times', 10), command=self.load)
        Play = Button(window, text='Play', width=10, font=('Times', 10), command=self.play)
        Pause = Button(window, text='Pause', width=10, font=('Times', 10), command=self.pause)
        Stop = Button(window, text='Stop', width=10, font=('Times', 10), command=self.stop)
        Next = Button(window, text='Next', width=10, font=('Arial', 10), command=self.play_next)
        Loop = Button(window, text='Loop', width=10, font=('Arial', 10), command=self.loop)
        playlist = Button(window, text='Playlist', width=10, font=('Arial', 10), command=self.show_playlist)

        Load.place(x=10, y=20)
        Play.place(x=110, y=20)
        Pause.place(x=220, y=20)
        Stop.place(x=110, y=60)
        Next.place(x=10, y=100)
        Loop.place(x=220, y=100)
        playlist.place(x=110, y=100)

        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename()

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False

    def stop(self):
        mixer.music.stop()

    def play_next(self):
               pass

    def loop(self):
        if not self.playing_state==False:
            pass
        else:
            mixer.music.play(-1)

    def show_playlist(self):
        playlist_window = Toplevel()
        playlist_window.title("Playlist")
        playlist_window.geometry("300x200")
        
        playlist_listbox = Listbox(playlist_window, selectmode=SINGLE, width=40, height=10)
        playlist_listbox.pack(pady=10)
        
        for track in self.track_playlist:
            playlist_listbox.insert(END, track)


root = Tk()
app = MusicPlayer(root)
root.mainloop()
