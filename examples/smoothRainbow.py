# Example showing use of HSV colors
import time
from neopixel import Neopixel

numpix = 8
pinnum = 16
strip = Neopixel(numpix, 0, pinnum, "GRB")

hue = 0
while(True):
    color = strip.colorHSV(hue, 255, 150)
    strip.fill(color)
    strip.show()
    
    hue += 150