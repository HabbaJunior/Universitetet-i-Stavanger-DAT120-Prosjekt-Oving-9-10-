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
        else:
            try:
                self.starttidspunkt = datetime.fromisoformat(starttidspunkt)
            except:
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
        c = input("Skirv inn starttidspunktet til avtalen (YYYY-MM-DD HH:MM:SS): ")
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
            x = x.strip()
            y = y.strip()
            u = u.strip()
            o = o.strip()
            return(x, y, u, o)
        
        
def avtalerDenneDatoen(ListeMedAvtaler, Dato):
    with open(ListeMedAvtaler, "r", 1, "UTF-8") as LMA:
        ListeMedAvtalerSammeDato = []
        Dato = datetime.fromisoformat(Dato)
        for linje in LMA:
            x, y, u, o = linje.split(",")
            u = u.strip()
            try:
                u = datetime.fromisoformat(u)
            except:
                continue
            datetime.date(Dato) == datetime.date(u)
            ListeMedAvtalerSammeDato.append(x)
            return ListeMedAvtalerSammeDato

def LiknendeTittel(ListeMedAvtaler, søkeord):
    with open(ListeMedAvtaler, "r", 1, "UTF-8") as LMA:
        ListeMedAvtalerMedLiknendeTittel = []
        for linje in LMA:
            x, y, u, o = linje.split(",")
            x = x.strip()
            if x.find(søkeord) > -1 :
                ListeMedAvtalerMedLiknendeTittel.append(x)

def menyen():
                    
               
a = avtale("A", "B","2022-09-16 13:15:12" , 30) 
b = avtale ("B")
c = avtale ("C")                      
avtalene = [a, b, c]


printliste(avtalene)
eksporterliste(avtalene)

x, y, u, o = importerliste("AvtalerListeImport.txt")
avtale = avtale(x, y, u, o)

o = avtalerDenneDatoen("AvtalerListeImport.txt", "2000-12-12 13:15:12")
  
        