# Build a pyramid-shaped tower given a positive integer number of floors. 
# A tower block is represented with "*" character.

def tower_builder(n_floors):
    return [('*' * (f * 2 - 1)).center(n_floors * 2 - 1) for f in range(1, n_floors + 1)]