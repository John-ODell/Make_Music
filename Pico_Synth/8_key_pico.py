from machine import Pin, PWM
from time import sleep

# Define the buzzer pins
buzzer1 = PWM(Pin(13))  # Buzzer 1 on GPIO 13
buzzer2 = PWM(Pin(12))  # Buzzer 2 on GPIO 12

# Define a dictionary of notes and their frequencies within the octave C4 to C5
notes = {
    16: 261.63,  # C4
    17: 293.66,  # D4
    18: 329.63,  # E4
    19: 349.23,  # F4
    20: 392.00,  # G4
    21: 440.00,  # A4
    22: 493.88,  # B4
    26: 523.25   # C5
}

# Setup touch keys with the corresponding GPIO pins
keys = {
    16: Pin(16, Pin.IN, Pin.PULL_DOWN),
    17: Pin(17, Pin.IN, Pin.PULL_DOWN),
    18: Pin(18, Pin.IN, Pin.PULL_DOWN),
    19: Pin(19, Pin.IN, Pin.PULL_DOWN),
    20: Pin(20, Pin.IN, Pin.PULL_DOWN),
    21: Pin(21, Pin.IN, Pin.PULL_DOWN),
    22: Pin(22, Pin.IN, Pin.PULL_DOWN),
    26: Pin(26, Pin.IN, Pin.PULL_DOWN)
}

def play_tone(buzzer1, buzzer2, frequency):
    buzzer1.freq(int(frequency))
    buzzer2.freq(int(frequency))
    buzzer1.duty_u16(32768)  # 50% duty cycle
    buzzer2.duty_u16(32768)  # 50% duty cycle

def stop_tone(buzzer1, buzzer2):
    buzzer1.duty_u16(0)  # Turn off the buzzer
    buzzer2.duty_u16(0)  # Turn off the buzzer

while True:
    key_pressed = False
    for pin, key in keys.items():
        if key.value() == 1:
            print(f"Key pressed: {pin}, Note: {notes[pin]}")
            play_tone(buzzer1, buzzer2, notes[pin])
            key_pressed = True
            break
        else:
            print(f"Key {pin} not pressed")
    if not key_pressed:
        stop_tone(buzzer1, buzzer2)
    sleep(0.01)  # Small delay to prevent CPU overload
