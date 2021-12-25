from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import filedialog as fd
import shutil
from pygame import mixer

paused = False
list_songs = []
mixer.init()


def open_file():
    filenames = fd.askopenfilenames(title="MP3 CHOOSER", initialdir="/", filetypes=[("WAV Files", "*.wav")])
    songs = list(filenames)
    for song in songs:
        shutil.copy(song, "Music")
        songName = song.split("/")[-1]
        songs.append(songName)
        list_songs.insert(END, songName)


def play():
    global list_songs
    song = list_songs.get(ACTIVE)
    song = f'C:/Users/Victor/PycharmProjects/mp3Player/Music/{song}'

    mixer.music.load(song)
    mixer.music.play()


def stop():
    global paused
    if paused:
        mixer.music.unpause()
        paused = False
    else:
        mixer.music.pause()
        paused = True


def play_next():
    # to get the selected song index
    next_one = list_songs.curselection()
    print(next_one)
    # to get the next song index
    next_one = next_one[0] + 1
    # to get the next song
    temp = list_songs.get(next_one)
    temp = f'C:/Users/Victor/PycharmProjects/mp3Player/Music/{temp}'

    mixer.music.load(temp)
    mixer.music.play()
    list_songs.selection_clear(0, END)
    # activate newsong
    list_songs.activate(next_one)
    # set the next song
    list_songs.selection_set(next_one)

def Previous():
    # to get the selected song index
    previous_one = list_songs.curselection()
    # to get the previous song index
    previous_one = previous_one[0] - 1
    # to get the previous song
    temp2 = list_songs.get(previous_one)
    temp2 = f'C:/Users/Victor/PycharmProjects/mp3Player/Music/{temp2}'

    mixer.music.load(temp2)
    mixer.music.play()
    list_songs.selection_clear(0, END)
    # activate new song
    list_songs.activate(previous_one)
    # set the next song
    list_songs.selection_set(previous_one)


window = Tk()
window.title("WAV PLAYER")
window.config(padx=20, pady=20, height=300, width=300, bg="black")


next_img = PhotoImage(file="img/next.png")
pause_img = PhotoImage(file="img/pause.png")
play_img = PhotoImage(file="img/play.png")
previous_img = PhotoImage(file="img/previous.png")

# Listbox

list_songs = Listbox()
list_songs.config(borderwidth=5, activestyle=NONE, fg="white",
                  bg="grey", font=("Arial", 15, "bold"), selectforeground="#03f8fc",
                  selectbackground="#fc0a5f", selectborderwidth=5, selectmode=SINGLE)

list_songs.grid(row=1, column=0, columnspan=5, pady=5)

# Buttons
next_btn = Button(image=next_img, command=play_next)
pause_btn = Button(image=pause_img, command=stop)
play_btn = Button(image=play_img, command=play)
previous_btn = Button(image=previous_img, command=Previous)
select_btn = Button(text="Select Song", command=open_file)
select_btn.grid(row=0, column=1)

previous_btn.grid(row=2, column=0)
pause_btn.grid(row=2, column=1)
play_btn.grid(row=2, column=2)
next_btn.grid(row=2, column=3)



window.mainloop()