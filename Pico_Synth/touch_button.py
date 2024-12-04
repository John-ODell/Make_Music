from machine import Pin
from time import sleep

# Setup touch key on GPIO pin 16
touch_key = Pin(16, Pin.IN, Pin.PULL_DOWN)

while True:
    if touch_key.value() == 1:
        print("Touch button on pin 16 is pressed")
    else:
        print("Touch button on pin 16 is not pressed")
    sleep(0.5)  # Small delay to prevent CPU overload
