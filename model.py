import random

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        self.crke = [] if crke == None else crke

    def napacne_crke(self):
        seznam_napacne_crke = []
        for crka in self.crke:
            if crka not in self.geslo:
                seznam_napacne_crke.append(crka)
        return seznam_napacne_crke   

    def pravilne_crke(self):
        seznam_pravilne_crke = []
        for crka in self.crke:
            if crka in self.geslo:
                seznam_pravilne_crke.append(crka)
        return seznam_pravilne_crke

    def stevilo_napak(self):
        napake = len(self.napacne_crke())
        return napake

    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
        else: return True


    def poraz(self):   
        napake = len(self.napacne_crke())  
        if napake >= STEVILO_DOVOLJENIH_NAPAK:
            return True
        else: return False    

    def pravilni_del_gesla(self): 
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += crka + ' '
            else: niz += '_' 
        return niz

    def nepravilni_ugibi(self):
        niz = ''
        for crka in self.crke:
            if crka in self.napacne_crke():
                niz += 'crka' + ' '
        return niz

    def ugibaj(self, velika_crka):
        velika_crka = velika_crka.upper()
        if velika_crka in self.crke:
            return PONOVLJENA_CRKA
        else: 
            if velika_crka in self.pravilne_crke():
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA
            else:
                if self.zmaga():
                    return ZMAGA        
                else: 
                    return PRAVILNA_CRKA
bazen_besed = []
with open('besede.txt', 'r') as dat:
    for vrstica in dat:
        bazen_besed.append(vrstica.upper().strip())  

def nova_igra():
    return Igra(random.choice(bazen_besed))

