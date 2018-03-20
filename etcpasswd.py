#!/usr/bin/env python3

def main():
    with open('/etc/passwd') as file:
        for line in file:
            print(line.strip().split(':'))
            
if __name__ == '__main__':
    main()
