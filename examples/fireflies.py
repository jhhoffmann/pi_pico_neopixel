import time
from neopixel import Neopixel
import random

numpix = 8
pinnum = 16
strip = Neopixel(numpix, 0, pinnum, "GRB")

colors_rgb = [
    (232, 100, 255),  # Purple
    (200, 200, 20),  # Yellow
    (30, 200, 200),  # Blue
    (150,50,10),
    (50,200,10),
]

# same colors as normaln rgb, just 0 added at the end
colors_rgbw = [color+tuple([0]) for color in colors_rgb]
colors_rgbw.append((0, 0, 0, 255))

# uncomment colors_rgbw if you have RGBW strip
colors = colors_rgb
# colors = colors_rgbw

max_len = 32
min_len = 16
#pixelnum, posn in flash, flash_len, direction
flashing = []

num_flashes = 5

FL_PIXEL = 0
FL_COLOR = 1
FL_COLOR_RED = 0
FL_COLOR_GREEN = 1
FL_COLOR_BLUE = 2
FL_LEN = 2
FL_COUNT = 3
FL_DIR = 4
FL_DIR_UP = 1
FL_DIR_DOWN = -1

for i in range(num_flashes):
    pix = random.randrange(0, numpix)
    col = random.randrange(0, len(colors))
    flash_len = random.randint(min_len, max_len)
    flashing.append([pix, colors[col], flash_len, 0, FL_DIR_UP])
    
strip.fill((0,0,0))

while True:
    strip.show()
    for fl_index in range(num_flashes):

        pix = flashing[fl_index][FL_PIXEL]
        brightness = (flashing[fl_index][FL_COUNT]/flashing[fl_index][FL_LEN])
        colr = (int(flashing[fl_index][FL_COLOR][FL_COLOR_RED]*brightness),
                int(flashing[fl_index][FL_COLOR][FL_COLOR_GREEN]*brightness),
                int(flashing[fl_index][FL_COLOR][FL_COLOR_BLUE]*brightness))
        strip.set_pixel(pix, colr)

        if flashing[fl_index][FL_LEN] == flashing[fl_index][FL_COUNT]:
            flashing[fl_index][FL_DIR] = FL_DIR_DOWN
        if flashing[fl_index][FL_COUNT] == 0 and flashing[fl_index][FL_DIR] == FL_DIR_DOWN:
            pix = random.randrange(0, numpix)
            col = random.randrange(0, len(colors))
            flash_len = random.randint(min_len, max_len)
            flashing[fl_index] = [pix, colors[col], flash_len, 0, 1]
        flashing[fl_index][FL_COUNT] = flashing[fl_index][FL_COUNT] + flashing[fl_index][FL_DIR]
        time.sleep(0.005)
