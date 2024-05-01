def spazi(n):
    for i in range(n):
        print()
    return

def i(a):
    try:
        intero=int(input(a))
    except ValueError:
        spazi(1)
        intero = i("Inserire un valore Intero: ")
    return(intero)

def r(a):
    try:
        reale=float(input(a))
    except ValueError:
        spazi(1)
        reale = r("Inserire un valore Reale: ")
    return(reale)

def s(a):
    stringa=str(input(a))
    return(stringa)

def b(a):
    y = lim_I(a,0,1)
    if (y == 1):
        x=True
    else:
        x=False
    return x

def l(a,sep = " ",c = " ", n = False):
    lista=s(a).strip(c).split(sep)
    if n != True:  
        pass
    else:
        for i in range(len(lista)):
            lista[i] = lista[i].capitalize()
    return (lista)

def lim_I(a,l1,l2):
    x = i(a)
    while (x<l1) or (x>l2):
        x=i("Valore sbagliato, deve essere compreso tra {0:} e {1:}: ".format(l1,l2))
    return x

def lim_R(a,l1,l2):
    x = r(a)
    while (x<l1) or (x>l2):
        x=r("Valore sbagliato, deve essere compreso tra {0:} e {1:}: ".format(l1,l2))
    return x

def stampa_MI(m):
    for i in range(len(max(m))):
        for j in range(len(m)):
            try:
                print(m[j][i], end = " ")
            except IndexError:
                print("   ", end = " ")     
        print()
    return

def stampa_MR(m):
    for i in range(len(max(m))):
        for j in range(len(m)):
            print(m[j][i], end = " ")
        print
    return
