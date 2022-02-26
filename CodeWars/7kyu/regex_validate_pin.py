# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain 
# anything but exactly 4 digits or exactly 6 digits.

import re

def validate_pin(pin):
    if '\n' in pin:
        return False
    else:
        return re.search('^(\d{4}|\d{6})$') != None