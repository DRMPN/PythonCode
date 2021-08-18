# Determines whether a provided credit card number is valid according to Luhn’s algorithm

from math import floor
from cs50 import get_int


def main():
    # get card number and length
    card_num = get_credit_card_number()
    card_length = get_nubmer_length(card_num)

    # calculate checksum
    card_checksum = calculate_card_checksum(card_num, card_length)

    # check checksum and type of card
    result = full_card_check(card_num, card_length, card_checksum)

    print(result)


# asks user for natural number
def get_credit_card_number():
    while True:
        card_num = get_int("Number: ")
        if (card_num > 0):
            return card_num


# returns length of the passed integer
def get_nubmer_length(number):
    return len(str(number))


# checks whether credit card number is range or not
def check_card_length(length):
    return (length >= 13 and length <= 16)


# calculates card checksum
def calculate_card_checksum(card_num, card_length):

    even = 0
    odd = 0

    for i in range(card_length):

        n = floor(card_num % 10)

        if (i % 2 == 0):

            even += n

        else:
            n *= 2

            if (n >= 10):
                n = floor(n / 10) + (n % 10)

            odd += n

        card_num /= 10

    total = (even + odd) % 10

    return total


# returns true if checksum is correct
def check_card_checksum(check_sum):
    return check_sum == 0


# returns credit card type
def get_credit_card_type(card_num):

    # get first two digits from a card number
    two_digits = int(str(card_num)[:2])

    if(34 == two_digits or 37 == two_digits):
        return "AMEX"
    elif(40 <= two_digits and 42 >= two_digits):
        return "VISA"
    elif(51 <= two_digits and 55 >= two_digits):
        return "MASTERCARD"
    else:
        return "INVALID"


# returns either credit card type or error
# return type is str
def full_card_check(card_num, card_length, card_checksum):
    if (check_card_checksum(card_checksum) and check_card_length(card_length)):
        return get_credit_card_type(card_num)
    else:
        return "INVALID"


if __name__ == "__main__":
    main()