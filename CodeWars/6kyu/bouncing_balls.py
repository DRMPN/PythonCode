# A child is playing with a ball on the nth floor of a tall building. 
# The height of this floor, h, is known.

def bouncing_ball(h, bounce, window):
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        n = 0
        jump = False
        while h > window:
            h = bounce * h
            n += 1
            if jump:
                n += 1
            jump = True
        return n
    else:
        return - 1