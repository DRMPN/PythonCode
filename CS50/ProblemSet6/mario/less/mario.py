# Print pyramid of height N in terminal

from cs50 import get_int

# ensure that input is in range of (0,8]
while True:
    height = get_int("Height: ")
    if height > 0 and height <= 8:
        break

# produce pyramid
for i in range(height):
    print(' ' * (height - (i + 1)), end='#' * (i + 1))
    print()