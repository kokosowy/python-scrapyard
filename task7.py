#!/usr/bin/env python3

import argparse

import lxml.etree
import requests

parser = argparse.ArgumentParser()
parser.add_argument('--waluta', '-w', type=str)
parser.add_argument('--ilosc', '-i', type=float)
parser.set_defaults(waluta='EUR', ilosc=5)

def main():
    args = parser.parse_args()

    print(args.waluta)    
    
    r = requests.get('http://www.nbp.pl/kursy/xml/a056z180320.xml')
    r.raise_for_status()
    
    xml = lxml.etree.XML(r.content)
    
    for tag in xml.findall('.//kod_waluty'):
        if tag.text == args.waluta:
            nazwa = tag.getparent().find('./nazwa_waluty').text
            kurs = tag.getparent().find('./kurs_sredni').text            
            print('nazwa: '+nazwa)
            print('kurs: '+kurs)
            wynik = args.ilosc / float(kurs.replace(',','.'))
            print('w EUR: '+str(wynik))
            return
            
if __name__ == '__main__':
    main()
