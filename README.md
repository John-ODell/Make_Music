Making Music with passive Buzzers by John O'Dell

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