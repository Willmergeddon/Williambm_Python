import mosquitto, random, urllib2


cl = mosquitto.Mosquitto("DAT205")
cl.connect("127.0.0.1")
cl.subscribe("simon/test")


def messageReceived(broker, obj, msg):
&	    global cl
&	    print("Message " + msg.topic + " containing: " + msg.payload)

cl.on_message = messageReceived
while (client != None): client.loop()
