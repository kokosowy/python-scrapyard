#!/usr/bin/env python3

import socket

def main():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('/tmp/socket'))
    sock.listen(1)
    while True:
        sc, addr = sock.accept()
        print('accepted {!r}'.format(addr))
        data = sc.recv(4096)
        print("recv'd {!r}".format(data))
        sc.sendall(data)
        sc.close()
        
if __name__ == '__main__':
    main()
