#!/usr/bin/env python3

import argparse  # optparse
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--count', '-c',
    type=int)
parser.add_argument('haslo', nargs='?')

parser.set_defaults(
    count=10,
    haslo=os.environ.get('HASLO', 'PYTHON'))

class Litera:
    def __init__(self, znak):
        self.znak = znak
        self.odkryta = False
        
    def print(self):
        print(self.znak if self.odkryta else '_', end=' ')
        
class Gra:
    def __init__(self, haslo, proby):
        self.litery = [Litera(i) for i in haslo.upper()]
        self.proby = proby

    def print(self):
        for litera in self.litery:
            litera.print()
        print(self.proby)
        
    def koniec_gry(self):
        '''
        >>> gra = Gra('qwe')
        >>> gra.koniec_gry()
        False
        '''
        return self.proby <= 0 or all(i.odkryta for i in self.litery)

    def odkryj(self, znak):
        znak = znak.upper()
        znaleziona = False
        for i in self.litery:
            if i.znak == znak:
                i.odkryta = True
                znaleziona = True
        if not znaleziona:
            self.proby -= 1

def main():
    args = parser.parse_args()
#   wisielec = Gra(os.environ.get('HASLO', 'PYTHON'))
#   wisielec = Gra(sys.argv[1])
    wisielec = Gra(args.haslo, args.count)
    while not wisielec.koniec_gry():
        wisielec.print()
        wisielec.odkryj(input())
    wisielec.print()
    print('koniec gry')
        
if __name__ == '__main__':
    main()
