import paho.mqtt.client as mqtt
from subscriber import subscribe
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")


def publish():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect("localhost", 1883, 60)
    """for i in range(3):
        client.publish('a/b', payload=i, qos=0, retain=False)
        print(f"send {i} to a/b")
        time.sleep(1)
    """
    if subscribe() == "on":
        state = "TOGGLE"
    client.publish('zigbee2mqtt/0x385b44fffe164f57/set', payload=state, qos=0, retain=False)

    client.loop_forever()
