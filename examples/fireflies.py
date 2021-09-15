import time
from neopixel import Neopixel
import random

NUM_PIXELS = 8
PIN_NUM = 16
strip = Neopixel(NUM_PIXELS, 0, PIN_NUM, "GRB")

class Firefly:
    COLORS = [
        (232, 100, 255),
        (200, 200, 20),
        (30, 200, 200),
        (150, 50, 10),
        (50, 200, 10),
    ]

    MAX_LENGTH = 32
    MIN_LENGTH = 4
    
    DIR_UP = 1
    DIR_DOWN = -1
    
    def __init__(self, num_pixels):
        self.num_pixels = num_pixels
        self.pixel = random.randrange(0, self.num_pixels)
        self.color = random.randrange(0, len(Firefly.COLORS))
        self.length = random.randint(Firefly.MIN_LENGTH, Firefly.MAX_LENGTH)
        self.count = 0
        self.direction = Firefly.DIR_UP

    def get(self):
        brightness = self.count / self.length
        colorAtBrightness = tuple(int(brightness*c) for c in Firefly.COLORS[self.color])
        return (self.pixel, colorAtBrightness)

    def step(self):
        if self.length == self.count:
            self.direction = Firefly.DIR_DOWN
            
        if self.count == 0 and self.direction == Firefly.DIR_DOWN:
            self.__init__(self.num_pixels)
        else:
            self.count = self.count + self.direction

fireflies = []
for _ in range(NUM_PIXELS/2 + 1):
    firefly = Firefly(NUM_PIXELS)
    fireflies.append(firefly)

strip.fill((0,0,0))

while True:
    strip.show()
    time.sleep_ms(50)
    for firefly in fireflies:
        (pixel, color) = firefly.get()
        strip.set_pixel(pixel, color)
        firefly.step()
