import menu.funzioniutili as f #contiene le funzioni per gli input e le parti di codice usate più spesso
premessaggio = "Digitare" #prima parte del messaggio 
midmessaggio = "per" #terza parte del messaggio, la seconda è il numero da digitare
sep = "-"*40 #un separatore

funzioni = ("terminare","elenco docenti classe","orario docente","ore disponibili","docenti a lezione","<funzione>","<funzione>","<funzione>","<funzione>","<funzione>","<funzione>")
def creavoci(tup):
    
    """
    crea la lista con le opzioni possibili
    parametri:
    tup: una tupla con le funzioni che verranno usate

    return:
    ritorna una stringa formattata che contiene le opzioni
    """

    voce = ""
    for i in range(len(tup)):
        if (tup[i] != "<funzione>"):
            voce += f"{premessaggio} {i} {midmessaggio} {tup[i]}\n"
    return voce

def menu():
    """
    stampa le opzioni possibili "delimitate" da un separatore sopra e sotto
    non chiede parametri, non da return
    """
    menù = f"{sep}\n{creavoci(funzioni)}{sep}"
    print(menù)
    return 

def scelta(min,max):
    """
    stampa il menù e limita la scelta al numero di opzioni disponibili
    
    parametri:
    min: la scelta minima possibile
    max: la scelta massima possibile
    
    return:
    ritorna un intero che è la scelta effettuata
    """
    menu()
    scelta = f.lim_I("",min,max)
    return scelta
