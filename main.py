import slavescripts as op #Calls for the secondary scripts
import machine

#     Set Pinout Here
#     Should Be Formatted As Follows
#     led = Pin(28, Pin.Out)
#     or
#     name = Pin(Pin_Number, Pin_Type)

Switch_1 = Pin(9, Pin.IN, Pin.PULL_DOWN)
Switch_2 = Pin(10, Pin.IN, Pin.PULL_DOWN)
Switch_3 = Pin(14, Pin.IN, Pin.PULL_DOWN)
Switch_4 = Pin(15, Pin.IN, Pin.PULL_DOWN)
#Switch_5 = Pin(19, Pin.in, Pin.PULL_DOWN) #Remove comment if 5th Switch is incorporated

light_level = 1 # 0 is off, 1 is dim, 31 is max

def wheel(offset, brightness):
    offset = 255 - offset
    if offset < 85:
        return (255 - offset * 3, 0, offset *3, brightness)
    if offset <170:
        offset -= 85
        return (0, offset * 3, 255 - offset * 3, 0, brightness)
    offset -=170
    return (offset * 3, 255 - offset * 3, brightness)

#     Main Script Goes Here

def main():
    while True:     #     Runs Script Constantly
        if Switch_1.value():
            op.col_red()
        elif Switch_2.value():
            op.col_blue()
        elif Switch_3.value():
            op.col_green()
        elif Switch_4.value():
            op.colorfade()
        #elif Switch_5.value():
            #null
        elif Switch_1.value() & Switch_2.value():
            op.col_purple()
        elif Switch_1.value() & Switch_3.value():
            null
        elif Switch_1.value() & Switch_4.value():
            null
        #elif Switch_1.value() & Switch_5.value():
            #null
        elif Switch_2.value() & Switch_3.value():
            null
        elif Switch_2.value() & Switch_4.value():
            null
        #elif Switch_2.value() & Switch_5.value():
            #null
        elif Switch_3.value() & Switch_4.value():
            op.col_white()
        #elif Switch_3.value() & Switch_5.value():
            #null
        #elif Switch_4.value() & Switch_5.value():
            #null
        elif Switch_1.value() & Switch_2.value() & Switch_3.value():
            op.rainbow()
        elif Switch_1.value() & Switch_2.value() & Switch_4.value():
            op.rainfade()
        elif Switch_1.value() & Switch_3.value() & Switch_4.value():
            op.RGB()
        elif Switch_2.value() & Switch_3.value() & Switch_4.value():
            op.cus_col(0, 0, 0, light_level)
        elif Switch_1.value() & Switch_2.value() & Switch_3.value() & Switch_4.value():
            null
        else:
            op.off()

main()
