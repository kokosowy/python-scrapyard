#!/usr/bin/env python3

'''ćwiczenie 1, na tym etapie już dobrze przerobione

chodzi o funkcję wykres()'''

import sys

PRZYKLAD = '1435322412'

def wykres(a):
    '''rysujemy wykres słupkowy'''
    for j in range(9, -1, -1):
        for i in range(len(a)):
            # asd
            print(('#' if int(a[i]) > j else ' '), end='')
        print()
    
    print()
    print(a)
    
def main():
    wykres(PRZYKLAD)
    
    return 1
    
if __name__ == '__main__':
    sys.exit(main())
