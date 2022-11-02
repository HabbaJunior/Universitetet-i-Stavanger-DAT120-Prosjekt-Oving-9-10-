# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 08:32:17 2022

@author: Datamaskin

"""
from datetime import datetime
InternListeMedAvtaler = []

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
        if starttidspunkt == "Ikke satt":
            self.starttidspunkt = starttidspunkt
        if isinstance(starttidspunkt, datetime):
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
    print("\nHei! Du kan nå lage en ny avtale")
    a = input("Skirv inn navnet til avtalen: ")
    b = input("Skirv inn stedet til avtalen: ")
    while True:
        c = input("Skirv inn starttidspunktet til avtalen (YYYY-MM-DD HH:MM:SS): ")
        try:
            c = datetime.fromisoformat(c)
            break
        except:
            print("Husk korrekt format")
            continue

    while True:
        d = input("Skirv inn varigheten til avtalen (helt tall i minutter): ")
        try:
            d = int(d)
            break
        except:
            print("Husk korrekt format")
            continue
    InternListeMedAvtaler.append(avtale(a, b, c, d))
    return InternListeMedAvtaler


def printliste(liste, Overskrift = "Overskrift :)"):
    print(Overskrift)    
    for index in range(len(liste)):
            print (f"Avtalen: {liste[index]} har index: {index}")
            
def eksporterliste(filnavn):
        with open(filnavn, "w", 1, "UTF-8") as ALE:
            for index in range(len(InternListeMedAvtaler)):
                ALE.writelines(InternListeMedAvtaler[index].__repr__()+ "\n")
      
def importerliste(filnavn):
    while True:
        try:
            with open(filnavn, "r", 1, "UTF-8") as ALI:
                pass
        except:
            print("Filen ikke funnet")  
        with open(filnavn, "r", 1, "UTF-8") as ALI:    
            for linje in ALI:
                x, y, u, o = linje.split(",")
                x = x.strip()
                y = y.strip()
                u = u.strip()
                o = o.strip()
                InternListeMedAvtaler.append(x + ", " + y + ", " + u + ", " + o)
        return InternListeMedAvtaler
        break


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
    return ListeMedAvtalerMedLiknendeTittel


while True:
    print("\nMeny, Velg Tall fra:    1-5")
    print("Les inn avtaler fra fil: 1 \nSkriv avtalene til fil:  2 \nRegistrer ny avtale:     3 \nPrint alle avtalene:     4 \nAvslutt:                 5")
    
    while True:
        valg = input("Ditt valg:               ")
        try:
            valg = int(valg)
            if 0 < valg <= 5:
               break
            else:
                continue
        except:
            print("Venligst bruk bare tall mellom 1 og 5")
            continue
 
    if valg == 1: #Les inn avtaler fra fil
        navnpafil = input("Skriv inn navnet på filen du vil importere: ")
        importerliste(navnpafil+".txt")
        
    
    if valg == 2: #Skriv inn avtaler til en fil 
        navnpafil = input("Skriv navnet på filen du vil eksportere til: ")
        eksporterliste(navnpafil)      
         
    if valg == 3: #Registrer ny avtale 
        nyavtale()
    
    if valg == 4: #Print ut avtalene 
       printliste(InternListeMedAvtaler)
       
    if valg == 5: #avslutt
        break 
                   
listen = ["apekatt", "jaaa", "ahahah", "rompe"]
liste2 = []
#liste2 = importerliste(avtalerlisteeksport)
#menyen()



"""               
a = avtale("A", "B","2022-09-16 13:15:12" , 30) 
b = avtale ("B")
c = avtale ("C")                      
avtalene = [a, b, c]


printliste(avtalene)
eksporterliste(avtalene)

x, y, u, o = importerliste("AvtalerListeImport.txt")
avtale = avtale(x, y, u, o)

o = avtalerDenneDatoen("AvtalerListeImport.txt", "2000-12-12 13:15:12")

Lister[input("Navnet pa listen min: ")] = listex
""" 
        