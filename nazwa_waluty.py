#!/usr/bin/env python3

import argparse

import lxml.etree
import requests

#

parser = argparse.ArgumentParser()
parser.add_argument('kod_waluty')
parser.add_argument('ilosc', type=float)

def main():
    args = parser.parse_args()
    
    r = requests.get('http://www.nbp.pl/kursy/xml/a056z180320.xml')
    r.raise_for_status()
    
    xml = lxml.etree.XML(r.content)
    
    for tag in xml.findall('.//kod_waluty'):
        if tag.text == args.kod_waluty:
            kurs = tag.getparent().find('./kurs_sredni').text
            kurs = float(kurs.replace(',', '.'))
            
            print('{} zł = {:.2f} {}'.format(
                args.ilosc, args.ilosc / kurs, args.kod_waluty))
            
            
if __name__ == '__main__':
    main()
