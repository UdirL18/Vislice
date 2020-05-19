#uvozimo random zaradi funkcije nova_igra
import random 


#KONSTANTE, ki jih ponavadi definiramo z velikimi tiskanimi črkami
STEVILO_DOVOLJENIH_NAPAK = 10

ZACETEK = 'Z'

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

    def ugibaj(self, ugibana_crka):
        ugibana_crka = ugibana_crka.lower()

        if ugibana_crka in self.crke:
            return PONOVLJENA_CRKA

        self.crke.append(ugibana_crka)
        
        if ugibana_crka in self.geslo: #vedmo da je pravilno uganil
            #uganil je
            if self.zmaga():
                return ZMAGA
            else: 
                return PRAVILNA_CRKA
            
        else: 
            if self.poraz():
                return PORAZ
            else: 
                return NAPACNA_CRKA
 

def nova_igra():
    return Igra(random.choice(bazen_besed))

class Vislice: #zaobsega več iger, skrbel bo za VEČ iger, imel bo več objektov igra
    def __init__(self,): #, ni pomembna
        #slovar ki ID-ju priredi igro
        self.igre = {} #slovar je funkcija ki slika iz int v objekt (igra, stanje) 

    def prosti_id_igre(self):
        #""" vrne nek id, ki ga ne uporablja nobena igra"""

        if len(self.igre) == 0: #če je slovar prazen potem sigurno id 0 ni v njem
            return 0
        else:
            return max(self.igre.keys()) + 1 #ključi so idji



    def nova_igra(self): #nova_igra mora narest novo igro tako da pridobi nov ID in zgnerira igro
        
        #dobimo svez id,
        nov_id = self.prosti_id_igre()

        #naredimo nov igro in
        sveza_igra = nova_igra()

        #vse to shranimo v self.igre
        self.igre[nov_id] = (sveza_igra, ZACETEK)

        #vrenemo id
        return nov_id


    def ugibaj(self, id_igre, crka):
        #vzamemo igro vn, odigramo potezo in shranimo nazaj noter
        #ko damo igro noter damo noter tudi posodobljeno stanje
        
        trenutna_igra,_ =self.igre[id_igre]

        #ugibamo crko 
        novo_stanje = trenutna_igra.ugibaj(crka)

        #zapišemo posodobljeno stanje in igro nazaj v BAZO 
        self.igre[id_igre] = (trenutna_igra, novo_stanje)




        
            





