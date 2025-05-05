import paho.mqtt.client as mqtt

class MQTTPublisher:
    def __init__(self, broker='localhost', topic='edge/events'):
        self.client = mqtt.Client()
        self.client.connect(broker)
        self.topic = topic

    def publish(self, message):
        self.client.publish(self.topic, message)

