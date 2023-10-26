import paho.mqtt.client as mqtt

# Define the MQTT broker and topic
broker_address = "broker.hivemq.com"
topic = "dlaw4608/home/classification/animal"

# Callback when the MQTT client successfully connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code "+str(rc))
    # Subscribe to the MQTT topic
    client.subscribe(topic)

# Callback for when a message is received from the MQTT topic
def on_message(client, userdata, msg):
    print("Received message: "+str(msg.payload.decode()))

# Initialize the MQTT client
mqtt_client = mqtt.Client()

# Set the MQTT callback functions
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Connect to the MQTT broker
mqtt_client.connect(broker_address, port=1883)

# Start the MQTT client loop to listen for messages
mqtt_client.loop_forever()