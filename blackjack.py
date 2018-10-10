import random

oznake = ("Pik","Herc","Tref","Karo")
rankovi = ("Dvojka","Trojka","Cetvorka","Petica","Sestica","Sedmica","Osmica","Devetka","Desetka","Zandar","Dama","Kralj","Kec")
vrednosti={"Dvojka":2,"Trojka":3,"Cetvorka":4,"Petica":5,"Sestica":6,"Sedmica":7,"Osmica":8,"Devetka":9,"Desetka":10,"Zandar":10,"Dama":10,"Kralj":10,"Kec":11}

igranje=True

class Karta:
    def __init__(self, rank, oznaka):
        self.rank=rank
        self.oznaka=oznaka

    def __str__(self):
        return self.rank+" "+self.oznaka

class Spil:
    def __init__(self):
        self.spil=[]
        for rank in rankovi:
            for oznaka in oznake:
                self.spil.append(Karta(rank,oznaka))
    
    def __str__(self):
        komp_spil=""
        for kart in self.spil:
            komp_spil+=str(kart)+"\n"
        return komp_spil

    def mesaj(self):
        random.shuffle(self.spil)
    
    def deli(self):
        zadnja_karta=self.spil.pop()
        return zadnja_karta

class Ruka:

    def __init__(self):
        self.spil=[]
        self.vrednost=0
        self.kec=0

    def dodaj_kartu(self,karta):
        self.spil.append(karta)
        self.vrednost+=vrednosti[karta.rank]
        if vrednosti[karta.rank]==11:
            self.kec+=1

    def podesavanje_za_keca(self):
        while self.vrednost>21 and self.kec:
            self.vrednost-=10
            self.kec-=1

class Cipovi:
    
    def __init__(self,total=100):
        self.total=total
        self.ulog=0

    def pobeda(self):
        self.total+=self.ulog
    
    def gub(self):
        self.total-=self.ulog

def opklada(cipovi):
    print('Cipovi na raspolaganju',igracovi_cipovi.total)
    while True:
        try:
            cipovi.ulog=int(input("Koliko cipova zelite uloziti: "))
        except ValueError:
            print("Unesite broj!")
        else:
            
            if cipovi.total<cipovi.ulog:
                print("Nemate toliko cipova. Cipovi na raspolaganju su: ",cipovi.total)
            else:
                break

def hit(spil,ruka):
    ruka.dodaj_kartu(spil.deli())
    ruka.podesavanje_za_keca()

def hit_stand(spil,ruka):
    global igranje

    while True:
        x=input("\nDa li zelite hit ili stand (kucajte 'h' ili 's'): ")
        if x[0].lower()=="h":
            hit(spil,ruka)
        elif x[0].lower()=="s":
            print("Igrac je standovao")
            igranje=False
        else:
            print("Probajte opet!")
            continue
        break

def igrac_busts(igrac,diler,cipovi):
    print("\nIgrac je bust!")
    cipovi.gub()

def igrac_pobeda(igrac,diler,cipovi):
    print("\nIgrac je pobedio!")
    cipovi.pobeda()

def diler_busts(igrac,diler,cipovi):
    print("\nDiler je bust!")
    cipovi.pobeda()
    
def diler_pobeda(igrac,diler,cipovi):
    print("\nDiler je pobedio!")
    cipovi.gub()
    
def nerseno(igrac,diler):
    print("\nNereseno")

def prikazi_neke(igrac,diler):
    print("\nDilerova ruka:")
    print(" <karta sakrivena>")
    print('',diler.spil[1])  
    print("\nIgracova ruka:", *igrac.spil, sep='\n ')
    
def prikazi_sve(igrac,diler):
    print("\nDilerova ruka:", *diler.spil, sep='\n ')
    print("Dilerova ruka =",diler.vrednost)
    print("\nIgracova ruka:", *igrac.spil, sep='\n ')
    print("Igracova ruka =",igrac.vrednost)
    
igracovi_cipovi=Cipovi()

while True:
    print("\nDobrodosli u BLACKJACK. Probajte da sto blize pridjete broju 21.\n")

    spil=Spil()
    spil.mesaj()

    igracova_ruka=Ruka()
    igracova_ruka.dodaj_kartu(spil.deli())
    igracova_ruka.dodaj_kartu(spil.deli())

    dilerova_ruka=Ruka()
    dilerova_ruka.dodaj_kartu(spil.deli())
    dilerova_ruka.dodaj_kartu(spil.deli())
    


    opklada(igracovi_cipovi)

    prikazi_neke(igracova_ruka,dilerova_ruka)

    while igranje:
        hit_stand(spil,igracova_ruka)

        prikazi_neke(igracova_ruka,dilerova_ruka)

        if igracova_ruka.vrednost>21:
            igrac_busts(igracova_ruka,dilerova_ruka,igracovi_cipovi)
            break

    if igracova_ruka.vrednost<=21:
        while dilerova_ruka.vrednost<17:
            hit(spil,dilerova_ruka)

        prikazi_sve(igracova_ruka,dilerova_ruka)

        if dilerova_ruka.vrednost>21:
            diler_busts(igracova_ruka,dilerova_ruka,igracovi_cipovi)

        elif dilerova_ruka.vrednost>igracova_ruka.vrednost:
            diler_pobeda(igracova_ruka,dilerova_ruka,igracovi_cipovi)
        
        elif dilerova_ruka.vrednost<igracova_ruka.vrednost:
            igrac_pobeda(igracova_ruka,dilerova_ruka,igracovi_cipovi)
        else:
            nerseno(igracova_ruka,dilerova_ruka)

    print("\nIgrac trenutno ima: ",igracovi_cipovi.total,"cipova")
    
    if igracovi_cipovi.total>0:

        nova_igra=input("Da li zelite novu igru (da ili ne): ")

        if nova_igra[0].lower()=='d':
            igranje=True
            continue
        else:
            break
    else:
        print ("Dovidjenja")
        break
