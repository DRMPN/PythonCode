#word to alphabetical order
s=""
o=''.join(sorted(s))
c="abcdefghijklmnopqrstuvwxyz"

def MC(a):
    '''
    test Middle-Character
    '''
    mc = a
    if len(mc) % 2 == 0:
        return (mc[len(mc) // 2 - 1])
    else: 
        return (mc[len(mc) // 2])

if MC("o") == c[len(c) // 2 - 1]:
    print("we won")
else:
    print("we lost")
