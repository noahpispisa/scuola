import modulo_orario.docenti as docenti_classe
import menu.menu as menu
import menu.funzioniutili as f
def main():

    """
    funzionamento 
    tramite il modulo "menù" faccio comparire un menù all'utetnte e gli chiedo la funzione da eseguire
    chiedo, dopo che la scelta è stata effettuata, i dati all'utente tramite il modulo "funzioniutili"
    una volta inseriti tutti i dati eseguo la funzione e, in caso ci sia, do un messaggio di errore
    chiedo poi se l'utente vuole fare qualcos'altro(in caso non abbia scelto prima di terminare il programma) e, in caso, chiudo il programma

    variabili(oltre alla richiesta di parametri per la funzione da eseguire appena dopo)
    rip: un Booleno che serve a far ripetere il programma
    testo: il contenuto del file, è un a matrice
    s: la scelta effettuata dall'utente

    non da return
    """

    testo = docenti_classe.lettura_file("OrarioTabellaGlobale") #salvo il contenuto del file in una matrice
    rip = False
    while not rip: #ciclo per ripetere il programma 
        s = menù.scelta(0,4) #scelta di cosa eseguire
        if s == 0:
            rip = True
        elif s == 1:
            print("Dice i docenti dui una determinata classe\n")
            classe = ""
            while classe == "":
                classe = f.s("Inserire la classe: ").upper() 
            err = docenti_classe.docenti(testo,classe) #se la funzione ritorna un errore mando un messaggio
            if err != None:
                print("Classe non esistente")
        elif s == 2:
            print("Dice l'orario del docente e le ore di lezione\n")
            docente = ""
            while docente == "":
                docente = f.s("Inserire il docente ").upper()
            err = docenti_classe.orario_docente(testo,docente)
            if err != None:
                print("Il docente non è presente")
        elif s == 3:
            print("Dice il numero di ore a disposizione del docente\n")
            docente = ""
            while docente == "":
                docente = f.s("Inserire il docente ").upper()
            err = docenti_classe.cognome_nome(testo,docente)
            if err != None:
                print("Il docente non è presente")
        elif s == 4:
            print("Dice la lista e il numero di docenti che hanno lezione in una determinata ora di un determinato giorno\n")
            ora = f.lim_I("Inserire l'ora: ",1,8)
            giorno = ""
            while giorno == "":
                giorno = f.s("Inserire il giorno: ").capitalize()
            giorno = giorno[0:2]
            err = docenti_classe.docenti_lezione(testo,ora,giorno)
            if err != None:
                print("Giorno non valido")
        if rip != True:
            rip = f.b("Vuoi fare qualcos'altro? (1=si, 0=no) ")
            rip = not rip
    print("Grazie per aver eseguito il programma!")
    return

main()