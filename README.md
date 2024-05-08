# Progetto orario
## Sviluppato e documentato da
[Pispisa Noah](https://github.com/noahpispisa) e [Cortella Michael](https://github.com/michaelCortella)

## Cosa fa:
Questo programma mostra un menù all'utente da coui ha le opzioni di scelta,
una volta effettuata chiede i dati necessari per la funzione da eseguire,
una volta immessi correttamente la esegue per poi chiedere se si vuole ripetere il programma.
Genera e/o modifica dei file.txt 

## Posizione e nome file
Vengono generati fino a 4 file, si troveranno nella **cartella da cui si ha fatto partire il programma**:
1. `docenti delle classi.txt`
2. `docenti orario.txt`
3. `docenti ore a disposizione.txt`
4. `docenti a lezione.txt`

## Cosa contiene:
**3 cartelle:**
1. documentazione, che contiene appunto la documentazione come file html generati da pydoc
2. menu, che contiene 3 file:
   -  `__init__.py` che rende la directory un pacchetto
   -  `menu.py` che contiene le funzioni per generare un menù
   -  `funzioniutili.py` che contiene le funzioni che vengono usate di più e in `main.py`
4. modulo_orario, che contiene 2 file:
   -  `__init__.py`
   -  `docenti.py`, che contiene le funzioni che vengono utilizzate in `main.py`

**2 file:**

- 1 file python:
  - `main.py`, nonchè il file da far partire per usare il programma
- 1 file CSV:
  - `OrarioTablellaGlobale.CSV`, il testo dato per svolgere il progetto.
