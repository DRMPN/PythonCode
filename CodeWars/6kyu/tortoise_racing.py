# More generally: given two speeds v1 (A's speed, integer > 0) and v2 
# (B's speed, integer > 0) and a lead g (integer > 0) 
# how long will it take B to catch A?

# The result will be an array [hour, min, sec] which is the time needed in 
# hours, minutes and seconds (round down to the nearest second) 
# or a string in some languages.

from math import floor

def race(v1, v2, g):
    if v1 >= v2:
        return None
    else:
        time = (g * 3600) / (v2 - v1)
    return [int(time / 3600), int((time % 3600) / 60), int(time % 60)]