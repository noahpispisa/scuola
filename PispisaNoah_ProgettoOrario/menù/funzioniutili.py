"""
il modulo contiene:
le fuinzioni per avere in input
    inetri
    reali
    booleani
    stringhe(una sintassi ppiù breve rispetta ad "input")
le funzioni che uso di più
    strip e split di una stringa
    stampa di matrici(sia regolari che non)
"""

def spazi(numero = 3):

    """
    genera un n numero di spazi
    
    parametri:
    numero: il numero di spazi
    
    non da return"""
    
    for i in range(numero):
        print()
    return

def i(frase = "Inserisci un intero: "):
    
    """
    contina a chiedere un intero finchè non gliene viene dato uno
    
    parametri:
    frase: la frase di cortesia

    return:
    ritorna il numero intero inserito dall'utente
    """

    try:
        intero=int(input(frase))
    except ValueError:
        spazi(1)
        intero = i("Inserire un valore Intero: ")
    return(intero)

def r(frase = "Inserisci un reale: "):

    """
    continua a chiedere un numero reale, smette quando ne viene inserito uno
    
    parametri:
    frase: la frase di cortesia
    
    return:
    ritorna il numero reale inserito dall'utente
    """

    try:
        reale=float(input(frase))
    except ValueError:
        spazi(1)
        reale = r("Inserire un valore Reale: ")
    return(reale)

def s(frase = "Inserisci una stringa: "):

    """
    chiede una stringa
    abbreviazione dell'input standard di python(come sintassi)

    parametri:
    frase: frase di cortesia

    return:
    ritorna la stringa inserita dall'utente
    """

    stringa=str(input(frase))
    return(stringa)

def b(frase = "Inserisci un boleano(1 = True, 0 = False): "):

    """
    chiede un booleano, se si mette 0 è "False", se si mette 1 è "True"
    
    parametri:
    frase: la frase di cortesia
    
    return:
    il booleano corrispondente all'input dell'utente
    """

    valore1 = lim_I(frase,0,1)
    if (valore1 == 1):
        valore=True
    else:
        valore=False
    return valore

def l(frase,sep = " ",ecc = " ", nomi = False):

    """
    chiede una striga che verrà poi splittata e splittata, se si specifica che è un insieme di nomi mette le iniziali in maiuscolo
    
    parametri:
    frase: la frase di cortesia
    sep: il separatore(una stringa)
    ecc: "eccesso" ovvero la parte da strippare
    nomi: un booleano per capire se è un insieme di nomi o meno
    
    return:
    la lista di stringhe data la stringa ioniziale inserita dall'utente
    """

    lista=s(frase).strip(ecc).split(sep)
    if nomi == True:  
        for i in range(len(lista)):
            lista[i] = lista[i].capitalize()
    return (lista)

def lim_I(frase,min,max):

    """
    chiede un valore intero entro un limite
    
    parametri:
    min: il limite minimo
    max: il limite massimo
    
    retun:
    ritorna la scelta dell'utente
    """

    valore = i(frase)
    while (valore<min) or (valore>max):
        valore=i(f"Valore sbagliato, deve essere compreso tra {min} e {max}: ")
    return valore

def lim_R(frase,min,max):

    
    """
    chiede un valore reale entro un limite
    
    parametri:
    min: il limite minimo
    max: il limite massimo
    
    retun:
    ritorna la scelta dell'utente
    """

    x = r(frase)
    while (frase<min) or (frase>max):
        x=r(f"Valore sbagliato, deve essere compreso tra {min} e {max}: ")
    return x

def stampa_MI(matrice):

    """
    stampa di una matrice irregolare
    
    parametri:
    matrice: la matrice
    
    non da return
    """

    for i in range(len(max(matrice))):
        for j in range(len(matrice)):
            try:
                print(matrice[j][i], end = " ")
            except IndexError:
                print("   ", end = " ")     
        print()
    return

def stampa_MR(matrice):

    """
    stampa di una matrice regolare
    
    parametri:
    matrice: la matrice
    
    non da return
    """
    
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            print(matrice[j][i], end = " ")
        print
    return
