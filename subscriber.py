
import paho.mqtt.client as mqtt
import json
import pygame
import time
import os
from musicplayer import playmusic

playlist = []
# The callback function of connection

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("zigbee2mqtt/0xf082c0fffe2e242a")

# The callback function for received message
def on_message(client, userdata, msg):
    json_string = str(msg.payload.decode("utf-8","ignore"))
    dictionary = json.loads(json_string)
    if dictionary["action"] == "brightness_move_up": 
        state = "ON"
        client.publish('zigbee2mqtt/0x385b44fffe164f57/set', payload=state, qos=0, retain=False)
        playmusic()

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:    # A track has ended
                print(playlist)
                if len ( playlist ) > 0:       # If there are more tracks in the queue...
                    pygame.mixer.music.queue ( playlist.pop() ) # Q



    elif dictionary["action"] == "on":
        state = "OFF"
        client.publish('zigbee2mqtt/0x385b44fffe164f57/set', payload=state, qos=0, retain=False)
        pygame.mixer.music.stop()
def subscribe():

    #
    pygame.display.init()
    screen = pygame.display.set_mode ( ( 420 , 240 ) )
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost", 1883, 60)
    client.loop_forever()
