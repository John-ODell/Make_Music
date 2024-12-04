Making Music with passive Buzzers by John O'Dell
--Update-- 12/4/2024 -> New Synth Update, Scroll Below for instructions. 

Arduino_Scale_Example

Items needed

    - Arduino uno (tested on r4)
    - Raspbery Pi Pico (Test on Pi Pico 2)
    - Passive buzzer module (two preffered and used in sketch)
    - Jumper Wire

Pin Outs

Buzzer 1
    - signal -> Pin 2
    - GND -> GND
    - VCC -> 3.3v

Buzzer 2

    - signal -> Pin 3
    - GND -> GND
    - VCC -> 3.3v

Download the Arduino IDE Platform https://www.arduino.cc/en/software

Open the sketch "arduino_scale_example"

    - Compile and write to your device
    - On Buzzer one C major scale with play with half notes in two onvtices
    - On Buzzer two C major scale will play with Whole notes in two octives

Python Example

Pin Outs

Buzzer 1
    - signal -> Pin 20
    - GND -> GND
    - VCC -> 3.3v

Buzzer 2

    - signal -> Pin 19
    - GND -> GND
    - VCC -> 3.3v

Download the Thonny IDE Platform https://thonny.org/
    
** Follow the Flash Instructions Below To install Micropython onto your Device **

Open the sketch "passive_buzzer_music_test"

    - Press the green arrow
    - On Buzzer one C major scale with play with half notes in two onvtices
    - On Buzzer two C major scale will play with Whole notes in two octives

TROUBLESHOOTING

    - Make sure that your wires are correct for sketch
    - You may get feedback from just signal wires, make sure vcc and ground are in
    - keep to 3.3v on the arduino
    - Some buzzer modules are not good enough quality
    - to increase or quite the noise, change the duty cycle
    - notation is based off 440A and modern tunings. 

** Flashing MicroPython **

    - Open Thonny
    - Navigate to the top left
     - click run
      - configure interpreter 
      - on the bottom right
        - install Micropython
            - Target Volume will be chosen
            - Micrpython Family (RP2 for Raspberry Pi/Your device Family)
            - Variant (Check the Manufacturer)
            - Version, Most recent
            - Install
    - Afer the flash is done exit out of the Interpreter Pages
    - Click on run again
        - Configuer Interpreter
        - "Which Kind of INterpreter should Thonny use"
            - Micropython for your model device (some models will be automatically dedectied)
        - "Port or WebREPL"
            - COMS(number)
            - This number may have changed from when you ran through this the first time.
            - Click Ok
    - On the Thonny home page, Click the Red stop Sign
    - In the Shell below, You will see your device.


---- Pi Pico Synth - 10 Key Bread Board Synth by John O'Dell ----
Updated 12/4/2024

Items needed

    - 10 Touch Input models (feel free to change the inputs, I found touch to be the best for input time, 10 inputs needed)
    - 2 Passive Buzzers (based on how loud you want your Synth to be)
    - Pi Pico 2 with Micropython
    - Thonny IDE
    - ~40 Jumper Wires
    - 2 Breadboards (Recommended for Button Placement but can be done with 1)

This Sketch requires your inputs to be accesseble at all times, please think about how you are wiring so there are not any false inputs.

Pin Outs 

    - All Modules will use a common 3.3v and GND
    - It is easiest to "pick a side" for each module
        - Touch inputs
            - VCC -> 3.3v
            - GND -> 3.3v
            - S -> GPIO 16 - GPIO 22, GPIO 26-28 
                - 10 sequintial pins for easy orginization
        - Passive Buzzers
            - VCC -> 3.3v
            - GND -> GND
            - S -> GPIO 12 - GPIO 13
                - 2 sequintal pins for two buzzers, add more for more sound. I found two is good for personal playing.

    

Touch Button Example

This example is to make sure your inputs are working

    - open "touch_button.py" and press the green arrow
    - when you press a button in the serial monitor it will return a button has been pressed
    - Change the Pin number in the top the check if all your buttons are working

TROUBLESHOOTING

    - Make Sure you have not switched the VCC and the GND
    - The number is not the pin number but eh GPIO number, refer to the Raspberr Pi Pico pinout sheet

8 Key example

In this example We use 8 touch buttons and turn them into the "White keys" of a piano by assigning them each to a note of the C major scale.
We anchor this tuning based on A4 (fourth octive) at A 440hz. From this we can find the tuning of our different keys. We have a high sample rate for self regulation of Timing rather than a set BPM

    - Open "8_key.py" and press the green arrow
    - starting with the input assigned to GPIO 16, we play a major C scale.
    - In the serial monitor there will be a high refresh rate showing when a button is pressed along with the frequency associated with it

TROUBLESHOOTING

    - make sure you have VCC and GND correct
    - Make sure you are in the Correct GPIO pins
    - if wired in parrallel, there could be a power issue, wiring pin for pin I found has a better sound

--- Pi Pico Synth by John O'Dell ----

This is a mini Synth that has uses 10 touch inputs with passive buzzers to achieve two full ovtives of a piano/synth. 
8 Inputs are assigned the me C major scale, with one Input raising them a half step and another raising them an octive.
This is a fun exmperimental instrument that has a particular 8 bit sound to it.

    - Follow the main wiring diagram 
    - Open "mod_8_key.py" and press the green arrow
        - to play on boot, save the file to the Pi Pico device and name it "boot.py"
            - to get out of a boot cycle, refer to the  **Flashing MicroPython** Section
    
    - Feel Free to change the assigned tones to the keys to make a new set scale.
    - The modulating buttons can be changed as well in their current function, or a totally new one.
    
Practice Song:

    - (refer the the GPIO Pins)
        - |16 18 20|16 18 20|17 19 21|17 19 21|17 19 22|17 19 22|19 21 26|19 21 26|
    - (Refer to the Notes)
        -|C E G| C E G| D F A| D F A| D F B| D F B| E A C| E A C|
