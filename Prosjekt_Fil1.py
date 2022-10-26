# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 08:32:17 2022

@author: Datamaskin

"""
from datetime import datetime

class avtale:
    def __init__(self, tittel, sted = "Ikke satt", starttidspunkt = "Ikke satt", varighet = -1):
        self.settittel(tittel)
        self.setsted(sted)
        self.setstarttidspunkt(starttidspunkt)
        self.setvarighet(varighet) 
    
    def __str__(self):
        if self.varighet == -1:
            return f"Avtalen \"{self.tittel}\" holdes i  \"{self.sted}\", starter \"{self.starttidspunkt}\" og varer i \"Ikke satt\""
        else:
            return f"Avtalen \"{self.tittel}\" holdes i  \"{self.sted}\", starter \"{self.starttidspunkt}\" og varer i \"{self.varighet}\""
    
    def __repr__(self):
        return f"{self.tittel}, {self.sted}, {self.starttidspunkt}, {self.varighet}"
    
    
    def settittel(self, tittel):
        self.tittel = tittel.strip()
    
    def setsted(self, sted):
        self.sted = sted.strip()
    
    def setstarttidspunkt(self, starttidspunkt):
        if starttidspunkt.strip() == "Ikke satt":
            self.starttidspunkt = starttidspunkt
        elif type(starttidspunkt) is datetime:
            self.starttidspunkt = starttidspunkt.strip()
        else:
            raise TypeError("Avtalen forventer \"datetime\" som starttidspunkt")
    
    def setvarighet(self, varighet):
        while True:
            try:
                self.varighet = int(varighet)
            except:
                raise TypeError("Avtalen forventer \"int\" som varighet")
            break
        
        
        
def nyavtale():
    print("Hei! Du kan nå lage en ny avtale")
    a = input("Skirv inn navnet til avtalen: ")
    b = input("Skirv inn stedet til avtalen: ")
    while True:
        c = input("Skirv inn starttidspunktet til avtalen (AAAA-MM-DD TT:MM:SS): ")
        try:
            d = datetime.fromisoformat(c)
            break
        except:
            print("Husk korrekt format")
            continue
    while True:
        e = input("Skirv inn varigheten til avtalen (helt tall i minutter): ")
        try:
            e = int(e)
            break
        except:
            continue
    return avtale(a, b, d, e)


def printliste(liste):
    for index in range(len(liste)):
        print(liste[index] ,"den har index:",  index)

def eksporterliste(liste):
    with open("AvtalerListeEksport.txt", "w", 1, "UTF-8") as ALE:
        for index in range(len(liste)):
            ALE.writelines(avtalene[index].__repr__()+ "\n")
      
def importerliste(liste):
    with open(liste, "r", 1, "UTF-8") as ALI:
        for linje in ALI:
            x, y, u, o = linje.split(",") 
            return(x, y, u, o) 
        
a = avtale("A") 
b = avtale ("B")
c = avtale ("C")                      
avtalene = [a, b, c]

printliste(avtalene)
eksporterliste(avtalene)

x, y, u, o = importerliste("AvtalerListeImport.txt")
avtale = avtale(x, y, u, o)
        
        