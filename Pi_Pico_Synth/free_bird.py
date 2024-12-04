from machine import Pin, PWM
from time import sleep

# Define the buzzer pins
buzzer1 = PWM(Pin(20))  # Reassigned to pin 20
buzzer2 = PWM(Pin(19))  # Reassigned to pin 19

# Define a dictionary of notes and their frequencies
notes = {
    'A5': 880.00,
    'A#5': 932.33, 'Bb5': 932.33,
    'B5': 987.77,
    'C6': 1046.50,
    'C#6': 1108.73, 'Db6': 1108.73,
    'D6': 1174.66,
    'D#6': 1244.51, 'Eb6': 1244.51,
    'E6': 1318.51,
    'F6': 1396.91,
    'F#6': 1479.98, 'Gb6': 1479.98,
    'G6': 1567.98,
    'G#6': 1661.22, 'Ab6': 1661.22,
    'A6': 1760.00,
    'A#6': 1864.66, 'Bb6': 1864.66,
    'B6': 1975.53,
    'C7': 2093.00,
    'C#7': 2217.46, 'Db7': 2217.46,
    'D7': 2349.32,
    'D#7': 2489.02, 'Eb7': 2489.02,
    'E7': 2637.02,
    'F7': 2793.83
}

def play_tone(buzzer, note, duration):
    frequency = notes[note]
    buzzer.freq(int(frequency))
    buzzer.duty_u16(32768)  # 50% duty cycle
    sleep(duration)
    buzzer.duty_u16(0)  # Turn off the buzzer

# Define the melody
melody = [
    ('A5', 0.2, buzzer1), ('D6', 0.2, buzzer2), ('A5', 0.2, buzzer2), ('D6', 0.33, buzzer2),
    ('D6', 0.33, buzzer2), ('D6', 0.33, buzzer1), ('A5', 0.1, buzzer1), ('D6', 0.33, buzzer1),
    ('D6', 0.1, buzzer2), ('F6', 0.4, buzzer2), ('D6', 0.33, buzzer1), ('D6', 0.33, buzzer1),
    ('D6', 0.33, buzzer1), ('F6', 0.5, buzzer1), ('D6', 0.5, buzzer1), ('F6', 0.5, buzzer1),
    ('D6', 0.5, buzzer1), ('C6', 0.5, buzzer1), ('C6', 0.5, buzzer1), ('B5', 0.5, buzzer1),
    ('A5', 0.5, buzzer1), ('B5', 0.5, buzzer2), ('C6', 0.5, buzzer2), ('C#6', 0.5, buzzer1),
    ('C6', 0.5, buzzer1), ('E6', 0.5, buzzer1), ('A5', 0.5, buzzer1), ('C6', 0.5, buzzer1),
    ('A5', 0.5, buzzer1), ('C6', 0.5, buzzer1), ('C6', 0.5, buzzer1), ('C6', 0.5, buzzer1),
    ('B5', 0.5, buzzer1), ('A5', 0.5, buzzer1), ('B5', 0.5, buzzer2), ('C6', 0.5, buzzer2),
    ('C#6', 0.5, buzzer1), ('C6', 0.5, buzzer1), ('E6', 0.5, buzzer1), ('F7', 0.5, buzzer1)
]

# Play the melody
for note, duration, buzzer in melody:
    play_tone(buzzer, note, duration)
    sleep(0.1)
