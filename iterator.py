#!/usr/bin/env python3

class Cos:
    def __init__(self, koniec):
        self.koniec = koniec
    def __iter__(self):
        return Iterator(self.koniec)
        
class Iterator:
    def __init__(self, koniec):
        self.koniec = koniec
        self.stan = -1
        
    def __iter__(self):
        return self
        
    def __next__(self):
        self.stan += 1
        if self.stan >= self.koniec:
            raise StopIteration()
        return self.stan
        
def generator(koniec):
    i = 0
    while True:
        yield i
        i += 1
        if i >= koniec:
            return
