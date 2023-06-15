#importing libraries 
import os
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer
import pygame

# Create a GUI window
root = Tk()
root.title("Music Player")
root.geometry("920x600+290+85")
root.configure(background='#212121')
root.resizable(False, False)
mixer.init()
#pygame.display.init()

playlist = []

# Create a function to open a file
def AddMusic():
    path = "/home/ubuntu/Downloads/"
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.append(song)
def PlayMusic():
    
    print(playlist)
    music = playlist
    #mixer.music.load(playlist.pop())
    #mixer.music.queue(playlist.pop())
    #mixer.music.set_endevent(pygame.USEREVENT)
    #mixer.music.play()
    for i in music:
        mixer.music.load(i-1)
        mixer.music.play()
#while True:
#    for event in pygame.event.get():
#        if event.type == pygame.USEREVENT:    # A track has ended
#            if len ( playlist ) > 0:       # If there are more tracks in the queue...
#                pygame.mixer.music.queue ( playlist.pop() ) # Q


# icon
image_icon = PhotoImage(file="/home/ubuntu/Downloads/duck.png")
root.iconphoto(False, image_icon)
Top = PhotoImage(file="/home/ubuntu/Downloads/duck.png")
Label(root, image=Top, bg="#0f1a2b").pack()
# logo
logo = PhotoImage(file="/home/ubuntu/Downloads/duck.png")
Label(root, image=logo, bg="#0f1a2b", bd=0).place(x=70, y=115)


# Button
ButtonPlay = PhotoImage(file="/home/ubuntu/Downloads/button.png")
Button(root, image=ButtonPlay, bg="#0f1a2b", bd=0,
       command=PlayMusic).place(x=100, y=400)
ButtonStop = PhotoImage(file="/home/ubuntu/Downloads/button.png")
Button(root, image=ButtonStop, bg="#0f1a2b", bd=0,
       command=mixer.music.stop).place(x=30, y=500)
ButtonResume = PhotoImage(file="/home/ubuntu/Downloads/button.png")
Button(root, image=ButtonResume, bg="#0f1a2b", bd=0,
       command=mixer.music.unpause).place(x=115, y=500)
ButtonPause = PhotoImage(file="/home/ubuntu/Downloads/button.png")
Button(root, image=ButtonPause, bg="#0f1a2b", bd=0,
       command=mixer.music.pause).place(x=200, y=500)

# Label
Menu = PhotoImage(file="/home/ubuntu/Downloads/menu.png")
Label(root, image=Menu, bg="#0f1a2b").pack(padx=10, pady=50, side=RIGHT)
Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=330, y=350, width=560, height=250)
Button(root, text="Open Folder", width=15, height=2, font=("times new roman",
       12, "bold"), fg="Black", bg="#21b3de", command=AddMusic).place(x=330, y=300)
Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)

# Execute Tkinter
root.mainloop()
