import paho.mqtt.client as mqtt
import json
import webbrowser  

# The callback function of connection

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("zigbee2mqtt/0xf082c0fffe2e242a")

# The callback function for received message
def on_message(client, userdata, msg):
    json_string = str(msg.payload.decode("utf-8","ignore"))
    dictionary = json.loads(json_string)
    if dictionary["action"] == "brightness_move_up": 
        url= 'https://www.youtube.com/watch?v=TU7V5_Jy-RI'  
        # Open the URL using open() function of module  
        webbrowser.open_new_tab(url)  
        state = "ON"
        client.publish('zigbee2mqtt/0x385b44fffe164f57/set', payload=state, qos=0, retain=False)
    elif dictionary["action"] == "on":
        state = "OFF"
        client.publish('zigbee2mqtt/0x385b44fffe164f57/set', payload=state, qos=0, retain=False)
def subscribe():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost", 1883, 60)
    client.loop_forever()
