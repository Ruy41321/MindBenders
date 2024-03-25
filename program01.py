# -*- coding: utf-8 -*-
'''
I Caponians, una specie aliena proviente da un non ben specificato
pianeta della galassia, stanno pianificando da un bel po' l'invasione
del pianeta Terra. Per farlo, hanno creato e installato in vari punti
del pianeta varie *mind bending machine*, macchine che riducono
l'intelligenza degli umani attraverso la rete telefonica [1].

Terminata la fase di riduzione dell'intelligenza umana, il prossimo
passo verso la conquista della Terra sara' lo sbarco sul nostro
pianeta, che avverra' non appena i Caponians avranno trovato dei punti
sufficientemente spaziosi per far atterrare le loro astronavi.

Un'astronave vista dall'alto puo' essere rappresentata come un
rettangolo di dimensioni W (larghezza) e H (altezza). Nel considerare
lo spazio necessario ad un'astronave per atterrare vanno pero' aggiunti
sui 4 lati del rettangolo 4 aree in piu'. Le aree in piu' sono una una
per lato.
Le aree sporgono tutte di una stessa quantita' D, per permettere di
aprire su ogni lato un portellone di sbarco. Ogni portellone e' quindi
largo quanto il lato dell'astronave su cui si trova e lungo D, su
qualunque lato si trovi.

I Caponians vorrebbero sbarcare con le loro astronavi in alcune nostre
citta', di cui hanno scaricato le rispettive mappe. Una citta' puo'
essere rappresentata come un'immagine rettangolare nera, in cui ogni
palazzo e' rappresentato come un rettangolo colorato (ogni palazzo ha
un colore che lo identifica univocamente).

Per definire gli ultimi dettagli del piano di sbarco, i Caponians
hanno bisogno di un algoritmo che, data la mappa di una citta' e un
elenco di astronavi definite come sopra, confermi oppure no se
ciascuna astronave ha abbastanza spazio per atterrare in quella citta',
aprire i suoi 4 portelloni e sbarcare il suo contenuto. Le astronavi
non atterrano contemporaneamente nella citta', quindi vanno valutate
separatamente le une rispetto alle altre.

(1) Quindi, data un'immagine nera (citta') con dei rettangoli colorati
pieni (quad) disegnati sopra, con ogni rettangolo di un colore
diverso da tutti gli altri, bisognera':

- determinare posizione, dimensioni e colore di ogni rettangolo
- salvare in un file di testo un rettangolo per riga
- nel file, ogni rettangolo e' rappresentato con una sequenza di 7 valori:
     x, y, w, h, r, g, b
  separati da virgole, in ordine di coordinata y (numero di riga)
  decrescente e, a parimerito, di x (pixel della riga) crescente.

(2) Successivamente, e' dato un file di testo contente N terne di
interi.  Ogni terna separata internamente e dalle altre terne da un
qualunque numero di spazi, tabulazioni o ritorni a capo. Ogni terna
rappresenta larghezza W, altezza H e distanza minima D (vedere sotto)
di un rettangolo (astronave) che si vorrebbe aggiungere all'immagine
al punto (1):

- restituire una lista di N valori booleani, l'i-esimo valore nella
lista e' True se nell'immagine c'e' abbastanza spazio per inserire
l'i-esimo rettangolo

- un rettangolo puo' essere inserito nell'immagine se esiste almeno una
posizione nell'immagine in cui c'e' abbastanza spazio (cioe' un'area
costituita interamente da pixel neri) per contenere il rettangolo
stesso, piu' le 4 "estensioni" del rettangolo, ossia i 4 portelloni
dell'astronave.

Ad esempio, se un'astronave da inserire ha 2 pixel di
larghezza e 3 di altezza e D = 2, bisognera' cercare uno spazio
nell'immagine adatto a contenere la seguente figura:

                              **
                              **
                            **++**
                            **++**
                            **++**
                              **
                              **

in cui i simboli + sono i pixel del rettangolo/astronave 2x3 e i *
sono i pixel delle 4 estensioni/portelloni

Esempio:
Data la seguente immagine rappresentata con un carattere per ogni
pixel, dove "." e' un pixel nero mentre caratteri diversi da "." sono
pixel colorati (*=rosso, +=verde):

**....
**....
......
......
....++
....++

Il file con i rettangoli trovati da voi salvato deve contenere le
righe:
4,4,2,2,0,255,0
0,0,2,2,255,0,0

e dati le seguenti astronavi:

(3, 3, 0)
(2, 2, 4)
(1, 1, 3)
(4, 2, 1)
(2, 4, 1)

verra' restituita la lista: [True, False, False, False, False]
infatti solo la prima astronave puo' atterrare ad esempio nella
zona marcata da 'X' (non ha sportelloni, infatti D = 0)

**.XXX
**.XXX
...XXX
......
....++
....++

mentre le altre non entrano nella mappa perche', pur avendo un punto
in cui possono atterrare, non possono aprire tutti i portelloni


[1] https://en.wikipedia.org/wiki/Zak_McKracken_and_the_Alien_Mindbenders)
'''

from pngmatrix import load_png8

def check_area(B, mappa, x, y, t, lungY, lungX):
    x1, y1 = x, y+t
    for num in range(B):
        while True:
            #print(y1, x1, y, t)
            if mappa[y1][x1] == 0:
                if x1-x == B-1:
                    return True
                else:
                    x1 += 1
            else:
                #print("l'astronave è sui palazzi nel pixel {} {}".format(y1,x1))
                return False
  
def check_sportelloni(B, H, D, mappa, x, y, lungY, lungX):
        #print(lungY, lungX)
    if D == 0: return True # non ha sportelli, se è riuscito ad atterrare è ok
    for n in range(x, x+B):
        d = 1 #iteratore lunghezza sportello
        #print("prima")
        #print(y,d,D)
        #print(d, y, x, n)
        while y-d >= 0 and mappa[y-d][n] == 0:
            if d == D:
                #operazione andata a buon fine (lato disponibile) proseguire con il prossimo lato                   
                break
            else:
                d += 1
        if y-d < 0:
            #if B==5: print("helooo")
            return False #lo sportello andrebbe fuori mappa
        if mappa[y-d][n] != 0:
            #if B == 5: print("eccomi") 
            return False #lo sportello andrebbe su un palazzo
        
    #if B == 5 and H == 5 and D == 4:
        #print("helooo")
    y1 = y+H-1
    for n in range(x, x+B):
        d = 1 #iteratore lunghezza sportello
        #print("prima")
        #print(y,d,D)
        #print(D, y, d, n)
        while y1+d < lungY and mappa[y1+d][n] == 0:
            #print(D, y, d, n)
            #print("sono qua")
            if d == D:
                #operazione andata a buon fine (lato disponibile) proseguire con il prossimo lato                   
                break
            else:
                d += 1
        if y1+d >= lungY:
            #print("eccomi")
            #print(D, y, d, n)
            return False #lo sportello andrebbe fuori mappa
        if mappa[y1+d][n] != 0:
            #print("helooo")
            #print(D, y, d, n)
            return False #lo sportello andrebbe su un palazzo
    
    for n in range(y, y+H):
        d = 1 #iteratore lunghezza sportello
        #print("prima")
        #print(d, y, x, n)
        while x-d >= 0 and mappa[n][x-d] == 0:
            if d == D:
                #print(d, y, x, n)
                #print("sono qua")
                #operazione andata a buon fine (lato disponibile) proseguire con il prossimo lato                   
                break
            else:
                d += 1
        if x-d < 0:
            #print("eccomi")
            return False #lo sportello andrebbe fuori mappa
        if mappa[n][x-d] != 0:
            #print("helooo")
            return False #lo sportello andrebbe su un palazzo    
    #print("heloo {}".format(D))
    
    x1 = x+B-1
    for n in range(y, y+H):
        d = 1 #iteratore lunghezza sportello
        #print("prima")
        #print(y,d,D)
        #print(d, y, x, n)
        while x1+d < lungY and mappa[n][x1+d] == 0:
            #print(d, y, x, n)
            #print("sono qua")
            if d == D:
                #operazione andata a buon fine (lato disponibile) proseguire con il prossimo lato                   
                break
            else:
                d += 1
        if x1+d >= lungY:
            #print("eccomi")
            #print(d, y, x, n)
            return False #lo sportello andrebbe fuori mappa
        if mappa[n][x1+d] != 0:
            #print("helooo")
            #print(x1+d, n)
            #print(d, y, x, n)
            return False #lo sportello andrebbe su un palazzo
    #if B == 2 and H == 2 and D == 5:
        #print(x,y)
    return True

def ex(file_png, file_txt, file_out):
    # determinare posizione, dimensioni e colore di ogni pixel
    citta = load_png8(file_png)
    rect = []
    mappa = []
    lungY = len(citta)
    lungX = len(citta[0])
    #print("--------------------------------")
    # definire altezza e larghezza  
    for y in range(lungY):
        mappa.append([])
        for x in range(lungX):
            if citta[y][x] == (0,0,0):
                mappa[y].append(0)
            else:
                mappa[y].append(1)
            
            if citta[y][x] != (0,0,0) and (x-1 < 0 or citta[y][x-1] !=  citta[y][x]) and (y-1 < 0 or citta[y-1][x] !=  citta[y][x]):
                color = citta[y][x]
                i = x+1
                f = True
                while f and i < lungX:
                    if color != citta[y][i]:
                        f=False
                        w=i-x
                    else:
                        i += 1
                if lungY == i:
                        w=i-x
                i = y+1
                f = True
                while f and i < lungY:
                    #print(citta[i][x], x, y)
                    if color != citta[i][x]:
                        f=False
                        h=i-y
                    else:
                        i += 1        
                if lungY == i:
                        h=i-y
                #print(w,h)
                rect.append([x, y, w, h, citta[y][x][0], citta[y][x][1], citta[y][x][2]])
    #for i in range(lungY):
        #print(mappa[i])
    #print("--------------------------------")
    rect.sort(key=lambda x: (-x[1], x[0]))
    #print(lungY,lungY,lungX,lungX)
    # salvare in un file di testo un rettangolo per riga
    with open(file_out, "w") as file:
        for arg in rect:
            stringa = str(arg[0])+","+str(arg[1])+","+str(arg[2])+","+str(arg[3])+","+str(arg[4])+","+str(arg[5])+","+str(arg[6])+"\n"
            file.write(stringa)
    
  # definire se un astronave puo atterrare in quella citta
    #ottengo la stringa contenente i dettagli delle astronavi
    with open(file_txt, "r") as file:
        stringa = file.read()
    #print(stringa)
    #print("--------------------------------")
    #formatto la stringa in modo da togliere \t, \n e spazi e li trasformo tutti in singole ","
    stringa = stringa.replace("\n", ",")
    stringa = stringa.replace(" ", ",")
    stringa = stringa.replace("\t", ",")
    while ",," in stringa:
        stringa = stringa.replace(",,", ",")
    #print("--------------------------------")
    #print(stringa)
    #trasformo la riga formattata in lista di sottoliste di interi in modo che ogni sottolista rappresenta un astronava e ognuno dei 3 valori rispettivamente la B, H e D
    string_list = stringa.split(',')
    if string_list[0] == '':
        string_list = string_list[1:]
    astronavi = [[int(num) for num in string_list[i:i+3]] for i in range(0, len(string_list), 3)]
    #print(astronavi)
   #defisco per ogni astronave se puo atterrare
    lista = [False]* len(astronavi)
    #print(lista)
    for i in range(len(astronavi)):
        B, H, D = astronavi[i][0], astronavi[i][1], astronavi[i][2]
        #print(B, H, D)
        
        for y in range(D, lungY):
            f=True
            y1 = y
            for x in range(D, lungX):
                x1 = x
                flag2 = False
                while True:
                  if x1 < lungX and y1 < lungY:
                    #print(x1)
                    if mappa[y1][x1] == 0:
                        if x1-x == B-1:
                            #print("l'astronave {} potrebbe entrare nell area che inizia con {} {}".format(i+1,y,x))
                            flag2 = True
                            for t in range(H):
                                if y+t >= lungY: 
                                    flag2 = False
                                    break
                                #if D <= y
                                res = check_area(B, mappa, x, y, t, lungY, lungX)
                                
                                if res == False:
                                    flag2 = False
                                    break #non se po fà ritorna al for di x e controlla partendo da un altro pixel
                            #questo if avviene solo in caso sia falso il precedente quindi solo se l'astronave puo almeno atterrare con sportelli chiusi
                            if flag2 == True:
                                #check sportelloni
                                flag2 = check_sportelloni(B, H, D, mappa, x, y, lungY, lungX)
                                if flag2 == False:
                                    break #non se po fà ritorna al for di x e controlla partendo da un altro pixel
                            break
                        else:
                            x1 += 1
                    else:
                        #print("l'astronave {} è sui palazzi nell area che inizia con {} {}".format(i+1,y,x))
                        break
                  else:
                      #print(x1,x)
                      #print("l'astronave {} finisce furi nell area che inizia con {} {}".format(i+1,y,x))
                      break
                #esco dal ciclo for x
                if flag2 == True:
                    lista[i] = True
                    break
            #esco dal for y
            if lista[i] == True:
                break
        
    #print(lista)
    
    # restituire una lista di N valori booleani, True se l'astronave può atterrare
    
    return(lista)

if __name__ == "__main__":
    print(ex("images/image10.png", "rectangles/rectangles10.txt", "test_output/example.txt"))
