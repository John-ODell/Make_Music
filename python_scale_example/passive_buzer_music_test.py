from machine import Pin, PWM
from time import sleep

# Define the buzzer pins
buzzer1 = PWM(Pin(20)) 
buzzer2 = PWM(Pin(19))

# Define a dictionary of notes and their frequencies
notes = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88,
    'C5': 523.25,
    'C5': 523.25,
    'D5': 587.33,
    'E5': 659.25,
    'F5': 698.46,
    'G5': 783.99,
    'A5': 880.00,
    'B5': 987.77,
    'C6': 1046.50
}

def play_tone(buzzer, note, duration):
    frequency = notes[note]
    buzzer.freq(int(frequency))
    buzzer.duty_u16(32768)  # 50% duty cycle
    sleep(duration)
    buzzer.duty_u16(0)  # Turn off the buzzer

# Define the C major scale
scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']

# Play the C major scale with Buzzer 1
for note in scale:
    play_tone(buzzer1, note, 0.2)
    sleep(0.1)

# Play the C major scale one octave higher with Buzzer 1
scale_high = ['C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6']
for note in scale_high:
    play_tone(buzzer1, note, 0.2)
    sleep(0.1)

# Play the C major scale with Buzzer 2 
for note in scale:
    play_tone(buzzer2, note, 0.5)
    sleep(0.1)

# Play the C major scale one octave higher with Buzzer 2
for note in scale_high:
    play_tone(buzzer2, note, 0.5)
    sleep(0.1)
