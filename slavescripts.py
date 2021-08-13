import time
import machine, apa102

strip = apa102.APA102(machine.Pin(19), machine.Pin(23), 60)

brightness = 1

def RGB():
    red = 0xff0000
    green = red >> 8
    blue = red >> 16
    for i in range(strip.n):
        colour = red >> (i % 3) * 8
        strip[i] = ((colour & red) >> 16, (colour & green) >> 8, (coulour & blue), brightness)
    strip.write()

def rainbow():
    for i in range(strip.n):
        strip[i] = wheel((i * 256 // strip.n) % 255, brightness)
    strip.write()
    
def rainfade():
    for r in range(5):
        for n in range(256):
            for i in range(strip.n):
                strip[i] = wheel(((i * 256 // strip.n) + n) & 255, brightness)
            strip.write()
        time.sleep_ms(25)

def colorfade():
    for b in range(31,-1,-1):
        strip[0] = (255, 153, 0, b)
        strip.write()
        time.sleep_ms(250)

def off():
    strip.fill((0, 0, 0, 0))
    strip.write()

def col_red():
    strip.fill((255, 0, 0, 1))
    strip.write()