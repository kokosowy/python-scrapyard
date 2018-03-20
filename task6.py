#!/usr/bin/env python3

import re

def sprawdz(tekst, maska, mode):
    regex = re.compile(maska)
    if mode == 'search':
        m = regex.search(tekst)
    elif mode == 'match':
        m = regex.match(tekst)
    print(m)
    if m:
        print('zawiera')
    else:
        print('nie zawiera')

""" 1

sprawdz('123', r'ziemniak', 'search')

"""

""" 2

sprawdz('asds', r'\d', 'search')

"""

""" 3
sprawdz('444', r'^\d*$', 'match')
"""

""" 4
sprawdz('444', r'^\d\d\d$', 'match')
"""

""" 5
sprawdz('84030900123', r'^\(d{2})([02468]-[1-9]|[15379][0-2](0[1-9]|[12][0-9]|3[0-1])$', 'match')
"""


