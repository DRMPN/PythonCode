# Print double pyramid of height N in terminal

from cs50 import get_int

# ensure that input is in range of (0,8]
while True:
    height = get_int("Height: ")
    if height > 0 and height <= 8:
        break

# produce pyramid
for i in range(height):
    # build left part of the pyramid
    print(' ' * (height - (i + 1)), end='#' * (i + 1))

    # keep distance between pyramids
    print('', end='  ')

    # build right part of the pyramid
    print('#' * (i + 1), end='')

    print()