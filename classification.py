from roboflow import Roboflow
import paho.mqtt.client as mqtt
import json

# Initialize the Roboflow API
rf = Roboflow(api_key="z3bLv3agEe4bA18wkkOA")
project = rf.workspace().project("animal-detection-rfktd")
model = project.version(1).model

# Initialize the MQTT client
mqtt_client = mqtt.Client()

# Define the MQTT broker and topic
broker_address = "broker.hivemq.com"
topic = "dlaw4608/home/classification/animal"

# Callback when the MQTT client successfully connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code "+str(rc))

# Callback for when the message is published to the MQTT topic
def on_publish(client, userdata, mid):
    print("Message published to MQTT topic")

# Set the MQTT callback functions
mqtt_client.on_connect = on_connect
mqtt_client.on_publish = on_publish

# Connect to the MQTT broker
mqtt_client.connect(broker_address, port=1883)

# Perform inference on an image
result = model.predict("images/two-elephants.jpeg").json()

# Convert the result to a JSON string
prediction_json = json.dumps(result)

# Publish the prediction as a JSON string to the MQTT topic
mqtt_client.publish(topic, prediction_json)

# Disconnect from the MQTT broker
mqtt_client.disconnect()
