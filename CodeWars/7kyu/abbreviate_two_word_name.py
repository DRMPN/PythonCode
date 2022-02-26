# Write a function to convert a name into initials. 
# This kata strictly takes two words with one space in between them.

def abbrev_name(name):
    a = name.split(' ')
    return f'{a[0][0].upper()}.{a[1][0].upper()}'