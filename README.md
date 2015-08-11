#MorseBerry
####MorseBerry is a python client-server app that sends messages to the Raspberry and it shows them in morse code, using leds and Raspberry GPIO pins.

To do this, two leds are used, a green one and a red one. The green led is on when a point ('.') is read. The red led is on when a hyphen ('-') is read. Both leds are on when a space (' ') is read.
The green led is connected to GPIO 17 and the red led to GPIO 27. 

Both leds are connected in series with a 1K resistor for protection of the Raspberry.

Run the server from the Raspberry to receive the messages and show them in LED morse:

``sudo ./server.py``

Run the client from another place to send messages:

``./client.py``

Don't forget to change the server and client parameters with the direction of your raspberry.
