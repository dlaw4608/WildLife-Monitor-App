const mqtt = require('mqtt');

// Define the MQTT broker and topic
const broker = 'mqtt://broker.hivemq.com';
const topic = 'dlaw4608/home/classification/animal';

// Initialize the MQTT client
const mqttClient = mqtt.connect(broker);

// Callback for when the MQTT client successfully connects to the broker
mqttClient.on('connect', () => {
    console.log('Connected to MQTT broker');

    // Subscribe to the MQTT topic
    mqttClient.subscribe(topic, (err) => {
        if (err) {
            console.error('Error subscribing to MQTT topic:', err);
        } else {
            console.log('Subscribed to MQTT topic');
        }
    });
});

// Callback for when a message is received from the MQTT topic
mqttClient.on('message', (topic, message) => {
    console.log('Received message:', message.toString());
});