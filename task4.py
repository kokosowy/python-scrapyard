#!/usr/bin/env python3

import pprint

"""

x = [i*2 for i in range(1,50)]
print(x)

"""


"""
x = [(i*2,i) for i in range(11)]
print(x)

"""

x = [[(i+j)%2 for i in range(8)] for j in range(8)]
pprint.pprint(x)


