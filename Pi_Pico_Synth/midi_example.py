from machine import Pin, PWM
from time import sleep
import usb_midi
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff

# Define the buzzer pins
buzzer1 = PWM(Pin(20))  # Reassigned to pin 20
buzzer2 = PWM(Pin(19))  # Reassigned to pin 19

# Define a dictionary of notes and their frequencies
notes = {
    69: 440.00,  # A4
    71: 493.88,  # B4
    72: 523.25,  # C5
    73: 554.37,  # C#5
    74: 587.33,  # D5
    76: 659.25,  # E5
    77: 698.46,  # F5
    79: 783.99,  # G5
    81: 880.00,  # A5
    83: 987.77,  # B5
    84: 1046.50, # C6
    85: 1108.73, # C#6
    86: 1174.66, # D6
    88: 1318.51, # E6
    89: 1396.91, # F6
    91: 1479.98, # F#6
    93: 1567.98, # G6
    94: 1661.22, # G#6
    96: 1760.00, # A6
    98: 1864.66, # A#6
    99: 1975.53, # B6
    101: 2093.00, # C7
    103: 2217.46, # C#7
    105: 2349.32, # D7
    106: 2489.02, # D#7
    108: 2637.02, # E7
    110: 2793.83, # F7
}

# Initialize MIDI input
midi = adafruit_midi.MIDI(midi_in=usb_midi.ports[0], in_channel=0)

def play_tone(buzzer, frequency, duration):
    buzzer.freq(int(frequency))
    buzzer.duty_u16(32768)  # 50% duty cycle
    sleep(duration)
    buzzer.duty_u16(0)  # Turn off the buzzer

while True:
    msg = midi.receive()
    if isinstance(msg, NoteOn) and msg.velocity > 0:
        note = msg.note
        if note in notes:
            frequency = notes[note]
            if note % 2 == 0:
                play_tone(buzzer1, frequency, 0.5)
            else:
                play_tone(buzzer2, frequency, 0.5)
    elif isinstance(msg, NoteOff) or (isinstance(msg, NoteOn) and msg.velocity == 0):
        # Stop playing the note
        buzzer1.duty_u16(0)
        buzzer2.duty_u16(0)
