# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 08:32:17 2022

@author: Datamaskin

"""
from datetime import datetime as dt

class avtale:
    def __init__(self, tittel, sted, starttidspunkt, varighet):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet
        
    def __str__(self):
        return f"Avtalen {self.tittel} holdes i {self.sted}, starter {self.starttidspunkt} og varer {self.varighet}"
    
    def settittel(self, tittel):
        self.tittel = tittel
    def setsted(self, sted):
        self.sted = sted
    def setstarttidspunkt(self, starttidspunkt):
        if isinstance(starttidspunkt, dt):
            self.starttidspunkt = starttidspunkt    
        else:
            raise TypeError("Avtalen forventer \"datetime\" som starttidspunkt")
    def setvarighet(self, varighet):
        while True:
            try:
                self.varighet = int(varighet)
            except ValueError("Avtalen forventer \"int\" som varighet"):
                break
            
k = dt.now()
abc = avtale("a", "b" , "c" , "d")
e = 15
abc.setstarttidspunkt(k)

print(abc)
        
        