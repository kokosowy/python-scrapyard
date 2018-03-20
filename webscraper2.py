#!/usr/bin/env python3

import re
import requests

def main():
    r = requests.get('http://onet.pl')
    r.raise_for_status()
    print('\n'.join(re.findall(r'<img [^>]*src="([^"]*)"', r.text)))
    
    
if __name__ == '__main__':
    main()
    
