#model za vislice imamo, sedaj potrebujemo tekstovni vmesnik ki bo pognal program

#uvozimo naš model.py 
import model 

trenutna_igra = model.nova_igra()

#kaj se zgodi med igro, koliko napak, koliko poskusov
def izpis_igre(igra):
    text = (
        f"Stanje gesla: {igra.pravilni_del_gesla()} \n"
        f"Imaš š {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()} možnosti za napako."
    )

    return text
    

def izpis_zmage(igra):
    return  (f"ZMAGAL SI, GESLO JE BILO; {igra.geslo}," +
            f"potreboval si {len(igra.napacne_crke())} ugibov.")

def izpis_poraza(igra):
    return  f"IZGUBIL SI, GESLO JE BILO; {igra.geslo}"


def zahtevaj_vnos():
    return input("Vpiši naslednjo črko:")

def pozeni_vmesnik():
    trenutna_igra = model.nova_igra()

    while True:
        #pokažemo mu stanje
        print(izpis_igre(trenutna_igra))

        crka = zahtevaj_vnos()

        trenutna_igra.ugibaj(crka)

        if trenutna_igra.zmaga():
            print(izpis_zmage(trenutna_igra))
            break #return None
        if trenutna_igra.poraz():
            print(izpis_poraza(trenutna_igra))
            break

