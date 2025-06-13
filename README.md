# USB HID
## Getting Started
### Ethical Use Only
This tool is intended to be used only for authorized testing and education. 

### Hardware
At a minimum you'll need a microcontroller capable of running circuit python. The one shown in the video is a Seeed Xiao RP2040 development board.

### Install Circuit Python
Download the utf file for your board [here](https://circuitpython.org/)
Place your board into bootloader mode (usually there is a boot button to press while plugging into a computer)
The board should show up as a USB drive, transfer the utf file to the drive. It will restart and show back up as a CIRCUITPY drive.

### Install required libraries
Download the Adafruit library bundle from [here](https://circuitpython.org/libraries)
Unzip it and copy it into the adafruit_hid folder into the lib folder on the CIRCUITPY drive.

### Modify and add code.py
Modify the code.py file to use your desired payload. If you want to use the powershell dropper from stage 1 you'll need to update the IP and host the second stage. Alternatively you can adjust to a single stage or whichever payload you'd like.
Copy the contents of the code.py into the code.py on the CIRCUITPY drive. When powered on the microcontroller will automatically execute whatever code is in the code.py file. 