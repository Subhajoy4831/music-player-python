import tkinter as tk
import fnmatch
import os
from pygame import mixer
from tkinter import ttk

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x600")
canvas.config(bg = "black")

rootpath = "C:\\Users\ghosh\Music\Yt to mp3"
pattern = "*.mp3"

mixer.init()

prev_img = tk.PhotoImage(file = "prev_img.png")
next_img = tk.PhotoImage(file = "next_img.png")
stop_img = tk.PhotoImage(file = "stop_img.png")
play_img = tk.PhotoImage(file = "play_img.png")
pause_img = tk.PhotoImage(file = "pause_img.png")

def select():
    if not mixer.music.get_busy() and playButton["text"] == "":
        label.config(text = listbox.get("anchor"))
        mixer.music.load(rootpath + "\\" + listbox.get("anchor"))
        mixer.music.play()
        playButton["text"] = "Pause"
        playButton["image"] = pause_img

    elif playButton["text"] == "Pause":
        mixer.music.pause()
        playButton["text"] = "Play"
        playButton["image"] = play_img
    
    else:
        mixer.music.unpause()
        playButton["text"] = "Pause"
        playButton["image"] = pause_img

def stop():
    mixer.music.stop()
    listbox.select_clear('active')
    label.config(text = "")
    playButton["text"] = ""
    playButton["image"] = play_img

def play_next():
    next_song = listbox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listbox.get(next_song)
    label.config(text = next_song_name)
    
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

def play_prev():
    prev_song = listbox.curselection()
    prev_song = prev_song[0] - 1
    prev_song_name = listbox.get(prev_song)
    label.config(text = prev_song_name)
    
    mixer.music.load(rootpath + "\\" + prev_song_name)
    mixer.music.play()

    listbox.select_clear(0,'end')
    listbox.activate(prev_song)
    listbox.select_set(prev_song)

listbox = tk.Listbox(canvas, fg = "cyan", bg = "black", width = 100, font = ('Arial',15))
listbox.pack(padx = 15, pady = 15)

label = tk.Label(canvas, text = '', bg = 'black', fg = 'yellow', font = ('Arial',18))
label.pack(pady = 15)

buttons = tk.Frame(canvas, bg= "black")
buttons.pack(padx = 10,pady = 5, anchor = 'center')

prevButton = tk.Button(canvas, text = "Prev", image = prev_img, bg = 'black', borderwidth = 0, command = play_prev)
prevButton.pack(pady = 15, in_ = buttons, side = 'left')

playButton = tk.Button(canvas, text = "", image = play_img, bg = 'black', borderwidth = 0, command = select)
playButton.pack(pady = 15, in_ = buttons, side = 'left')

nextButton = tk.Button(canvas, text = "Next", image = next_img, bg = 'black', borderwidth = 0, command = play_next)
nextButton.pack(pady = 15, in_ = buttons, side = 'left')

stopButton = tk.Button(canvas, text = "Stop", image = stop_img, bg = 'black', borderwidth = 0, command = stop)
stopButton.pack(pady = 15, in_ = buttons, side = 'left')

volume_label = tk.Label(canvas, text="Volume: 50%", bg = 'black', fg = 'white', font = ("Arial",15))
volume_label.pack(pady=5)

def setVolume(volume):
    mixer.music.set_volume(float(volume) / 100)
    volume_value = int(round(float(volume)))
    volume_label.config(text=f"Volume: {volume_value}%")

volume_slider = ttk.Scale(canvas, from_=0, to=100, orient=tk.HORIZONTAL, command=setVolume, length=300)
volume_slider.set(50)
volume_slider.pack(pady=10)

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listbox.insert('end', filename)

canvas.mainloop()