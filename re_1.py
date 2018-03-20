#!/usr/bin/env python3

import re

def main():
#   m = re.search(r'^([0-9][0-9])([02468][1-9]|[13579][0-2])(0[1-9]|[12][0-9]|3[0-1])([0-9]{4})([0-9])$', input('tekst> '))
#   m = re.search(r'^(PL)?[0-9-]{10}$', input('tekst> '))

    m = re.search(r'^https?://(www\.)?youtube\.com/.*[=/](\b[A-Za-z0-9_-]+)$', input('tekst> '))
    if m:
        print('TAK: ' + repr(m.group(2)))

if __name__ == '__main__':
    main()
