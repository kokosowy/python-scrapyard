#!/usr/bin/env python3

import re
import sys
import urllib.error
import urllib.request

def main():
    try:
        u = urllib.request.urlopen('http://www.onet111111111111111111111111111.pl/')
    except urllib.error.HTTPError as e:
        print(e.code)
        sys.exit(2)
    except urllib.error.URLError as e:
        print('nieprawidłowy url: ' + str(e.reason))
        sys.exit(1)
    
    data = u.read().decode()
    print('\n'.join(re.findall(r'<img [^>]*src="([^"]*)"', data)))
    
if __name__ == '__main__':
    main()
