#uvozimo random zaradi funkcije nova_igra
import random 

#KONSTANTE, ki jih ponavadi definiramo z velikimi tiskanimi črkami
STEVILO_DOVOLJENIH_NAPAK = 10

#konstante za rezultate
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

#konstante za zmago in poraz
ZMAGA = 'W'
PORAZ = 'X'


bazen_besed = []
with open('besede.txt', 'r') as dat:
    for vrstica in dat:
        bazen_besed.append(vrstica.lower().strip()) 


#RAZRED Igra
class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo.lower()
        self.crke = [] if crke == None else crke.lower() #če bomo že kaj uganili želimo da nadaljuje od tu
        # namesto none ne smemo pisati []

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

    def ugibaj(self, ugibana_crka):          #Metodo ugibaj, ki sprejme črko, jo pretvori v veliko črko, vrne PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA, ZMAGA, PORAZ
        mala_crka = ugibana_crka.lower()
        if mala_crka in self.crke: # v self.crke si shranjujemo ugibe
            return PONOVLJENA_CRKA
        else: 
            if mala_crka in self.pravilne_crke():
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA
            else:
                if self.zmaga():
                    return ZMAGA        
                else: 
                    return PRAVILNA_CRKA

 

def nova_igra():
    return Igra(random.choice(bazen_besed))

