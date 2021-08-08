from apa102_pi.driver import apa102

def clearStrip():
    strip = apa102.APA102(num_led=150, order='rgb')
    
    strip.clear_strip()