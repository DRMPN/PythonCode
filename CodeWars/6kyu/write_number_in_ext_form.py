# You will be given a number and you will need to return it as a string in Expanded Form.
# NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(num):
    i = 1
    res = []
    s = str(num)
    for c in s:
        n = c + '0' * (len(s) - i)
        if int(n) > 0: res.append(n)
        i += 1
    return ' + '.join(res)