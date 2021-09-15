import time
from neopixel import Neopixel
from firefly import Firefly

NUM_PIXELS = 8
PIN_NUM = 16
strip = Neopixel(NUM_PIXELS, 0, PIN_NUM, "GRB")

fireflies = []
for _ in range(int(NUM_PIXELS/2)):
    firefly = Firefly(NUM_PIXELS)
    fireflies.append(firefly)

strip.fill((0,0,0))
while True:
    for firefly in fireflies:
        (pixel, color) = firefly.get()
        strip.set_pixel(pixel, color)
        firefly.step()
    strip.show()
    time.sleep_ms(50)
