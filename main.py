#     Import Machine and Utime Script

from machine import Pin
import time

#     Import Color Files

import startup
import clear
import red
import purple

#     Set Pinout Here
#     Should Be Formatted As Follows
#     led = Pin(28, Pin.Out)
#     or
#     name = Pin(Pin_Number, Pin_Type)

Switch_1 = Pin(14, Pin.IN, Pin.PULL_DOWN)
Switch_2 = Pin(14, Pin.IN, Pin.PULL_DOWN)

#     Main Script Goes Here

def main():
    startup.start()
    time.sleep(10)
    clear.clearStrip()
    
    while True:     #     Runs Script Constantly
        if Switch_1.value():
            red.change()
        elif Switch_2.value():
            purple.change()
        elif Switch_1.value() && Switch_2.value():
            while True:
                red.change()
                time.sleep(2.5)
                purple.change()
                time.sleep(2.5)
        else:
            clear.clearStrip()
