#area of polygo n+ it's perimeter**2 rounded to 4 decimal places
import math
def polysum(n,s):
    return polyarper(n,s)
def polyarper(n,s):
        tan=math.tan(math.pi/n)
        up=0.25*n*s**2
        parea=up/tan
        pper=n*s
        ss=parea+(pper)**2
        ss=round(ss,4)
        return ss
print(polysum(38,26))
