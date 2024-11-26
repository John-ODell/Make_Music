#include <Arduino.h>

// Define the buzzer pins
const int buzzer1 = 2;  
const int buzzer2 = 3;  

// Define a dictionary of notes and their frequencies
const int NOTE_C4 = 261;
const int NOTE_D4 = 294;
const int NOTE_E4 = 330;
const int NOTE_F4 = 349;
const int NOTE_G4 = 392;
const int NOTE_A4 = 440;
const int NOTE_B4 = 494;
const int NOTE_C5 = 523;
const int NOTE_D5 = 587;
const int NOTE_E5 = 659;
const int NOTE_F5 = 698;
const int NOTE_G5 = 784;
const int NOTE_A5 = 880;
const int NOTE_B5 = 988;
const int NOTE_C6 = 1047;

void playTone(int buzzer, int note, int duration) {
  tone(buzzer, note, duration);
  delay(duration);
  noTone(buzzer);
}

// Define the C major scale
const int scale[] = {NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4, NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5};
const int scale_high[] = {NOTE_C5, NOTE_D5, NOTE_E5, NOTE_F5, NOTE_G5, NOTE_A5, NOTE_B5, NOTE_C6};

void setup() {
  pinMode(buzzer1, OUTPUT);
  pinMode(buzzer2, OUTPUT);

  // Play the C major scale with Buzzer 1 
  for (int i = 0; i < 8; i++) {
    playTone(buzzer1, scale[i], 200);
    delay(100);
  }

  // Play the C major scale one octave higher with Buzzer 1
  for (int i = 0; i < 8; i++) {
    playTone(buzzer1, scale_high[i], 200);
    delay(100);
  }

  // Play the C major scale with Buzzer 2 
  for (int i = 0; i < 8; i++) {
    playTone(buzzer2, scale[i], 500);
    delay(100);
  }

  // Play the C major scale one octave higher with Buzzer 2
  for (int i = 0; i < 8; i++) {
    playTone(buzzer2, scale_high[i], 500);
    delay(100);
  }
}

void loop() {
  // Nothing to do here
}
