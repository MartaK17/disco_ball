import paho.mqtt.client as mqtt
import json

import os
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer
from play import AddMusic
from play import PlayMusic

# Create a GUI window
root = Tk()
root.title("Music Player")
root.geometry("920x600+290+85")
root.configure(background='#212121')
root.resizable(False, False)
mixer.init()

# The callback function of connection

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("zigbee2mqtt/0xf082c0fffe2e242a")

# The callback function for received message
def on_message(client, userdata, msg):
    json_string = str(msg.payload.decode("utf-8","ignore"))
    dictionary = json.loads(json_string)
    if dictionary["action"] == "brightness_move":

        AddMusic()
        PlayMusic()

        state = "ON"
        client.publish('zigbee2mqtt/0x385b44fffe164f57/set', payload=state, qos=0, retain=False)
    elif dictionary["action"] == "on":
        mixer.music.stop()
        state = "OFF"
        client.publish('zigbee2mqtt/0x385b44fffe164f57/set', payload=state, qos=0, retain=False)
def subscribe():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost", 1883, 60)
    # Execute Tkinter
    root.mainloop()
    client.loop_forever()
