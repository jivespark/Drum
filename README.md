# Drum
This is going to be my project for week 3 of Hack Club half life. I built this project, because the task was to make an instrument, and I thought it would be cool to build a custom drum pad with a speaker to play the sounds.

## Design process:  
My first idea was that I just want to make a bunch of buttons for the drums, and a speaker to play all the sounds. The finished design was something pretty close to that, the only main difference from the original design, was that instead of regular buttons, I made custom footprints for capacitive touch buttons, directly in the PCB, so that I could have them in any shape/ layout that I wanted. I originally wanted to make a wider layout, with bigger buttons, but to fit within the JLCPC 100x100mm deal, I had to make it smaller, otherwise it would have been too expensive. After that the rest was pretty easy, I used an amplifier and a 40 mm speaker for the sound, and for the microcontroller I went with an ESP32 for it's capacitive touch inputs, and enough power to handle the audio files.

## Assembly+firmware:  
To assemble you just need to solder everything into the PCB, since all components are through hole, it shouldn't be too hard. You just need to screw the case on using M3 screws, and pop the speaker into the hole designed for it(note that the speaker hole might not be accurate, since I don't have the exact speaker yet, and they had no technical drawing available) The firmware is running on circuitpython, and can be downloaded [here](https://circuitpython.org/board/seeed_xiao_esp32s3/), after flashing that, you just need to upload everything in the firmware folder(code.py and the sounds folder) to the board, and you should be done.(note that the capacitive touch sensing may  need to be calibrated, but since I haven't built the project yet, I can't test exact calibration settings. This will be updated when I build the project).

## Images:  
Cad render:  
![Cad](https://github.com/jivespark/Drum/blob/main/Pictures/CAD.png?raw=true)
Schematic:  
![Schematic](https://github.com/jivespark/Drum/blob/main/Pictures/Schematic.png?raw=true)
PCB:  
![PCB](https://github.com/jivespark/Drum/blob/main/Pictures/PCB.png?raw=true)

##BOM
| Item                     | Qty | Supplier   | Cost/item | Total Cost | link                                                  |
|--------------------------|-----|------------|-----------|------------|-------------------------------------------------------|
| XIAO ESP32-S3            | 1   | Aliexpress | $10.57    | $10.57     | https://www.aliexpress.com/item/1005007870593864.html |
| MAX98357 audio amplifier | 1   | Aliexpress | $1.62     | $1.62      | https://www.aliexpress.com/item/1005009356741606.html |
| 40mm speaker             | 1   | Aliexpress | $2.86     | $2.86      | https://www.aliexpress.com/item/1005006335969407.html |
| PCB                      | 1   | JLCPCB     | $4.00     | $4.00      | https://jlcpcb.com/quote                              |
| Screws                   | 1   | Aliexpress | $2.08     | $2.08      | https://www.aliexpress.com/item/4000117933430.html    |
| Estimated total shipping | 1   |            |           | $9.00      |                                                       |
