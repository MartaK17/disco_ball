import pygame
import time
import os

#
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
def playmusic():

    AddMusic()
    pygame.display.init()
    screen = pygame.display.set_mode ( ( 420 , 240 ) )
    pygame.mixer.init()
    pygame.mixer.music.load ( playlist.pop() )  # Get the first track from the playlist
    pygame.mixer.music.play()           # Play the music
    for p in playlist:
        pygame.mixer.music.queue(p)
#    if len ( playlist ) > 0:       # If there are more tracks in the queue...
#        pygame.mixer.music.queue ( playlist.pop() ) # Q

#    pygame.mixer.music.queue ( playlist.pop() ) # Queue the 2nd song
    pygame.mixer.music.set_endevent ( pygame.USEREVENT )    # Setup the end track event
#    pygame.mixer.music.play()           # Play the music



#    for event in pygame.event.get():
#        if event.type == pygame.USEREVENT:    # A track has ended
#            if len ( playlist ) > 0:       # If there are more tracks in the queue...
#                pygame.mixer.music.queue ( playlist.pop() ) # Q


def starting():
    playmusic()

