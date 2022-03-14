def presses(phrase):
    keyboard = [
        '1',
        'ABC2',
        'DEF3',
        'GHI4',
        'JKL5',
        'MNO6',
        'PQRS7',
        'TUV8',
        'WXYZ9',
        '*',
        ' 0',
        '#'
    ]
    amount = 0
    for lttr in phrase.upper():
        for key in keyboard:
            try:
                i = key.index(lttr)
                i += 1
                amount += i
            except ValueError:
                pass
    return amount