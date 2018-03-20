#!/usr/bin/env python3

class Zwierze:
    def __init__(self, imie, kolor):
        self.imie = imie
        self.kolor = kolor
        
class Pies(Zwierze):
    def daj_glos(self):
        print(self.imie + ': Hau')
    
class Kot(Zwierze):
    def daj_glos(self):
        print(self.imie + ': Miau')


#------------------------------

class Czworokat:
    pass

class Trapez(Czworokat):
    def __init__(self, a):
        self.a = a
    
class Rownoleglobok(Trapez):
    pass
    
class Prostokat(Rownoleglobok):
    pass
    
class Deltoid(Czworokat):
    def __init__(self, a):
        self.a = a
    
class Kwadrat(Rownoleglobok, Deltoid):
    pass
