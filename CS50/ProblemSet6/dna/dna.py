# program that identifies a person based on their DNA

import sys
import csv


def main():

    # correct usage check
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # list of dictionaries
    database = []
    # read people's dna from a database
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for line in reader:
            database.append(line)

    # string of dna sequence
    sequence = ''
    # read dna sequence from a file
    with open(sys.argv[2]) as file:
        for line in file:
            sequence = line

    # calculate used tandems in sequence
    tandems = request_tandems(database[0], sequence)

    # try to find a person to match tandem repeats
    result = database_search(database, tandems)

    print(result)


# produces a list of locations of first element of tandem
def locate_tandems(sequence, tandem, tandem_length):
    tandem_list = []
    for i in range(len(sequence)):
        if sequence[i:i+tandem_length] == tandem:
            tandem_list.append(i)
    return tandem_list


# calculates amount of tandem in a list of tandemes
def count_tandems(tandem_list, tandem_length):

    # empty list case
    if not tandem_list:
        return 0

    count = 1
    max_count = 1

    for i in range(len(tandem_list) - 1):

        if tandem_list[i] == tandem_list[i+1] - tandem_length:
            count += 1
        else:
            count = 1

        max_count = max(max_count, count)

    return max_count


# calculates amount of particular tandem in sequence
def find_tandem_amount(sequence, tandem):
    tandem_length = len(tandem)

    tandem_list = locate_tandems(sequence, tandem, tandem_length)
    amount = count_tandems(tandem_list, tandem_length)

    return amount


# produces amount of tandems in sequence
def request_tandems(db_dic, sequence):
    tandem_dic = {}
    for tandem in list(db_dic)[1:]:
        tandem_dic[tandem] = find_tandem_amount(sequence, tandem)
    return tandem_dic


# linear search over all persons in database
def database_search(database, tandems):
    for person in database:
        if compare_tandems(person, tandems):
            return person['name']
    return "No match"


# compares person's tandems to sequence tandems
def compare_tandems(db_dic, tandem_dic):
    for tandem in list(tandem_dic):
        if int(db_dic[tandem]) != tandem_dic[tandem]:
            return False
    return True


if __name__ == "__main__":
    main()