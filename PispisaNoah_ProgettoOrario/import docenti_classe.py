import modulo_orario.docenti_classe as docenti_classe
import menù.modulo_menù as modulo_menù
import menù.funzioniutili as f
def main():
    testo = docenti_classe.lettura_file("OrarioTabellaGlobale")
    s = modulo_menù.scelta(0,4)
    if s == 0:
        classe = f.s("di quale classe si vogliono sapere i docenti? ")
    return

main()