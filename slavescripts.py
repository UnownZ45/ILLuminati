import time
import machine, apa102
import main

strip = apa102.APA102(machine.Pin(19), machine.Pin(23), 60)

brightness = light_level

RED1 = 0
GREEN1 = 0
BLUE1 = 0
BRIGHTNESS = 0

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

# COlOR PRESETS SHOULD FOLLOW THE FOLLOWING PATTERN
# def col_*color you want the preset to be*()
#*tab*strip.fill((RED, GREEN, BLUE, brightness))
#*tab*strip.write()

def col_red():
    strip.fill((255, 0, 0, brightness))
    strip.write()

def col_green():
    strip.fill((0, 255, 0, brightness))
    strip.write()

def col_blue():
    strip.fill((0, 0, 255, brightness))
    strip.write()

def col_purple():
    strip.fill((183, 93, 219, brightness))
    strip.write()

def col_white():
    strip.fill((255, 255, 255, brightness))
    strip.write()

def cus_col(RED1, GREEN1, BLUE1, BRIGHTNESS):
    strip.fill((RED1, GREEN1, BLUE1, BRIGHTNESS))
    strip.write()
