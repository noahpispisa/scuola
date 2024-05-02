def lettura_file(nomefile):

    '''
    La funzione pensa ad aprire il file, leggerlo riga per riga, formattarlo toglendo gli spazi da una riga all' altra e le ","
    per poi aggiungere l'elemento alla matrice righe creata in partenza

    parametri(nomefile)
    nomefile: si deve passare il nome del file di testo per poterlo aprire

    ritorna la lista con le righe del testo formattate
    '''

    righe = [] #creo la matrice che conterrà le righe
    file = open(f"{nomefile}.csv","r")
    riga = file.readline() 
    while(riga != ""):
        riga1 = riga.strip("\n")
        contenuto = riga1.split(",") #divido nei punti con la virgola
        righe.append(contenuto) #aggiungo la lista alla matrice
        riga = file.readline()
    file.close()
    return righe

def docenti(testo,classe):

    '''
    La funzione controlla che il file esista, in caso esistesse scorre il testo, cerca la classe data come parametro e 
    se la classe viene trovata aggiunge il nome del docente a una lista precedentemente creata.
    Successivamente aggiunge ogni elemento della lista formattandolo nel documento.

    parametri: (testo, classe)
    testo: si deve passare la matrice contenente tutte le righe del testo 
    classe: si deve passare la classe di cui controllare l'elenco docenti

    non sono presenti return, scrive nel file
    '''

    docenti_classe = [] #creo la lista che cotiene idocenti della classe
    for i in testo:
        if classe in i:
            docente = i[0].strip(" ") #rimuovo gli eventuali spazi a inizio e fine nome
            docenti_classe.append(docente) #aggiungo il docente alla lista
    if docenti_classe != []: #se la classe esiste
        file = open("docenti delle classi.txt","a")
        file.write(f"I docenti della classe {classe} sono:\n\n")
        for i in range(len(docenti_classe)):
            file.write(f"{docenti_classe[i]}\n") #scrivo nel file i docenti della classe
        file.write("\n")
        file.close()
    else: #return in caso di errore
        return -1
    return

def orario_docente(testo,docente):

    '''
    La funzione prova a creare un file di testo altrimenti se esiste lo legge, succesivamente legge il file riga per riga
    e crea la tabella dell' orario di un determinato docente e il numero di ore totali del docente

    parametri: (testo, docente)
    testo: matrice del testo gia strippato e separato
    docente: nome del docente da contrllare

    non sono presenti return, scrive nel file 
    '''

    presente = False
    for i in range(len(testo)): #cerco il docente nel testo
        if docente in testo[i][0]: #se è presente inserisco il suo orario 
            orario = list(testo[i])
            presente = True
    if presente != True:
        return -1
    else:
        try:
            f = open("docenti orario.txt","x+") #prova a creare il file
        except FileExistsError: #se esiste apre l'esistente in modalità lettura
            f = open("docenti orario.txt","r")
        riga = f.readline() #legge la prima riga
        if (riga == ""): # se è vuoto, chiude il file  e lo riapre in modalità scrittura, ci inserisce dento le prime due righe del file originale
            f.close()
            f1 = open("docenti orario.txt","w")
            for i in range(len(testo[0])):
                f1.write(f"{testo[0][i]}")
            f1.write("\n")
            for i in range(len(testo[1])):
                f1.write(f"{testo[1][i]}")
            f1.write("\n")
            f1.close() #chiude il file
        else: #se non è vuoto
            f.close() #chiude il file
        f = open("docenti orario.txt","a") #apro il file in modalità append
        for i in range(len(orario)):
            f.write(f"{orario[i]}")
        f.write("\n")
        while ("   " in orario): #rimuovo gli spazi vuoti
            orario.remove("   ")
        f.write(f"Le ore totali del docente sono: {(len(orario))-2}\n")
        f.close()
    return

def cognome_nome(testo, docente):

    '''
    Questa funzione scrive cognome e nome del docene inserito e controlla il totale delle ore a disposizione

    parametri(testo, docente):
    testo: matrice del testo gia strippato e separato
    docente: nome del docente da contrllare

    non sono previsti return, scrive nel file 
    '''

    presente = False #booleano per gestire gli erori(nel main) in caso mancasse il docente nel documento
    ContaOre= 0 #inizzializzo un contatore che mi servirà per le ore
    f=open("docenti ore a disposizione.txt", "a")  #apro il file in modalità append
    for i in range(2,len(testo)): #inizio a scorrere la matrice
        if docente in testo[i][0]: #controlla se all'interno della matrice è presente il nome dell' insegnante
            presente = True
            f.write(f"Le ore a disposizione del docente {docente} sono: ") #scrive il nome del docente
            for j in range(len(testo[i])): #scorro la lista in cui è presente l'insegnante preso da parmaetro
                if " D " in testo[i][j]:  #controlla se all' interno della lista del docente sono presenti ore a disposizione
                    ContaOre+=1 #aumento il contatore
            f.write(f"{ContaOre}\n\n") #scrivo le ore a disposizione del docente 
    f.close()
    if presente == False: #return in caso di errore
        return -1
    return

def docenti_lezione(testo,ora,giorno):


    '''
    La seguente funzione mostra un elenco di insegnanti che hanno lezione ad una determinata ora di un determinato giorno
    in seguito mostra anche quanti insegnanti hanno lezione a quell'ora

    parametri(testo,giorno,ora)
    testo: matrice del testo gia strippato e separato
    giorno: Il giorno da controllare
    ora: L'ora da controllare

    non sono previsti return, scrive direttamente sul file
    '''

    selezioneOra = 0 #counter per sapere quale elemento della lista corrisponde all'ora del giorno seleizonata
    for i in range(len(testo[0])):
        if giorno in testo[0][i]: #cerco la prima occorrenza del giorno e gli aggiungo l'ora sottratta di 1(sennò darebbe l'elemento appena dopo)
            selezioneOra = i+(ora-1)
            break
    if selezioneOra == 0: #se non è presente il giorno
        return -1
    else:
        Docenti = [] #creo la lista che conterrà i docenti
        f=open("docenti a lezione.txt", "a")
        for i in range(2,len(testo)):
            if (" R " not in testo[i][selezioneOra]) and ("   " not in testo[i][selezioneOra]):
                Docenti.append(testo[i][0]) #aggiungo i docenti che hanno lezione o disposizione
        f.write("I docenti che hanno lezione sono:\n")
        c = 0
        for i in range(len(Docenti)): #inserisco nel file()
            f.write(f"{Docenti[i]} ")
            c += 1
            if c%3 == 0: #per avere 3 docenti per riga
                f.write("\n")
        f.write("\n")
        f.write(f"Il numero di docenti che hanno lezione sono: {len(Docenti)}\n\n")
    return
