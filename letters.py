#!/usr/bin/env python3

import random
import sys

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'aa', 'ee', 'oo', 'uu', 'oe', 'ou', 'au', 'eu', 'ch', 'sch', 'ei',
           'ij', 'ui', 'aai', 'ooi', 'oei',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           'AA', 'EE', 'OO', 'UU', 'OE', 'OU', 'AU', 'EU', 'CH', 'SCH', 'EI',
           'IJ', 'UI', 'AAI', 'OOI', 'OEI']

while True:
    char = random.choice(letters)
    print('\n %s \n' % char)
    givenread = input('Volgende? ')
    if givenread == 'qq':
        sys.exit(0)
