# Produces minimum number of coins required to give a user change.

from cs50 import get_float


def main():

    change = handle_user_input()
    print(get_coins(change))


# get positive number from user
def handle_user_input():
    while True:
        change = get_float("Change owed: ")
        if (change >= 0):
            # rational number to natural
            return change * 100


# produce amount of coins to give
def get_coins(change):
    coins = 0
    while (change >= 25):
        change -= 25
        coins += 1
    while (change >= 10):
        change -= 10
        coins += 1
    while (change >= 5):
        change -= 5
        coins += 1
    while (change >= 1):
        change -= 1
        coins += 1
    return coins


if __name__ == "__main__":
    main()