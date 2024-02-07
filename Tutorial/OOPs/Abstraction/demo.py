# python doesn't support abstraction by default 

from abc import ABC

class Vehicle(ABC):
    def __init__(self, n):
        self.no_of_tyres = n
        
    def start(self):
        pass

class Bike:
    def __init__(self):
        self.no_of_tyres = 2
        
    def start(self):
        print("start with kicker")
        
class scooty:
    def __init__(self):
        self.no_of_tyres = 2
        
    def start(self):
        print("self start")
        
class car:
    def __init__(self):
        self.no_of_tyres = 4
        
    def start(self):
        print("start with key")
        
v = Vehicle()

v.start()
