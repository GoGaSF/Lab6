import time
import math

def calculate_square_root_after_delay(number, milliseconds):
    time.sleep(milliseconds / 1000)  
    square_root = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {square_root}")


number = 25100
milliseconds = 2123


calculate_square_root_after_delay(number, milliseconds)
