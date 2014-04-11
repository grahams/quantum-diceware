#!/usr/bin/env python

import quantumrandom
import csv
import argparse

from pkg_resources import Requirement, resource_filename

ID_LEN = 5
MAX_DIE_VALUE = 6

def _wordlist_to_dict(wordfile):
    with open(wordfile) as in_handle:
        d = {}
        for line in csv.reader(in_handle, delimiter="\t", quotechar='\''):
            d[line[0]] = line[1]
        return d

def main():
    parser = argparse.ArgumentParser(description="Generates passphrases.")

    parser.add_argument("numwords",
                            help="The number of words to generate")
    parser.add_argument("-s", "--separator", default=" ",
                            help="The separator to use between words")
    parser.add_argument("-f", "--wordfile",
                            help="Filesystem path to a dictionary")

    args = parser.parse_args()

    if(args.wordfile != None):
        worddict = _wordlist_to_dict(args.wordfile)
    else:
        worddict = _wordlist_to_dict(resource_filename(
        Requirement.parse("quantum_diceware"),
            "quantum_diceware/wordlists/english.asc"))

    numbers = []

    # for each word generate ID_LEN (5) random numbers (one for each 'die')
    for i in xrange(0, int(args.numwords)):
        dice = quantumrandom.uint16(ID_LEN)
        numbers.append("".join([str(y) for y in (dice % MAX_DIE_VALUE) + 1]))

    print args.separator.join([worddict[x] for x in numbers])

if __name__ == "__main__":
    main()
