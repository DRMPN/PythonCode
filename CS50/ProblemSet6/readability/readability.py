# Computes the approximate grade level needed to comprehend some text
# according to the Coleman-Liau formula
from cs50 import get_string


def main():
    # asks user for input
    text = get_string("Text: ")
    grade = calculate_readability(text)
    print(handle_grade(grade))


# calculates readability of the given text
def calculate_readability(text):

    letter_count = 0
    word_count = 1
    sentence_count = 0

    for i in range(len(text)):
        c = text[i]

        if (str.isalpha(c)):
            letter_count += 1

        if (c == ' '):
            word_count += 1

        if (is_punctuation_end(c)):
            sentence_count += 1

    # letters per 100 words
    L = letter_count / word_count * 100
    # sentences per 100 words
    S = sentence_count / word_count * 100

    # Coleman-Liau formula to calculate readability of a text
    index = round(0.0588 * L - 0.296 * S - 15.8)

    return index


# checks whether or not char is punctuation mark
def is_punctuation_end(c):
    return c == '.' or c == '!' or c == '?'


# return's user-frienldy output
def handle_grade(g):
    if (g < 0):
        return "Before Grade 1"
    elif (g >= 16):
        return "Grade 16+"
    else:
        return f"Grade {g}"


if __name__ == "__main__":
    main()