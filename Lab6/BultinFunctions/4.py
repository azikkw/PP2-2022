#Program that invoke square root function after specific milliseconds

import time

def after_time(number, after):
    time.sleep(after)
    sqrt_number = number ** 0.5
    
    print('Square root of 25100 after', int(after * 1000), 'miliseconds is', sqrt_number)
    
    
after_time(25100, 2.123)    