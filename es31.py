# Esercizio 31 
'''
Fornisci la rappresentazione in binario di un numero decimale. 
Dopo aver acquisito il valore del Numero da trasformare, si esegue la divisione del numero per 2 
e si calcola quoziente e resto. Il resto è la prima cifra della rappresentazione binaria. 
Si ripete il procedimento assegnando il quoziente ottenuto a Numero e ricalcolando la divisione per 2; 
la ripetizione prosegue mentre il quoziente ottenuto si mantiene diverso da zero. 
La rappresentazione binaria del numero decimale è costituita da cifre binarie ottenute come resti, 
lette in ordine inverso. Confronta poi il risultato con il valore ottenuto dalla funzione predefinita 
del linguaggio per convertire un numero decimale in binario. 
'''
import math

num = int(input("Qual è il numero decimale da trasformare? "))
n = num
binario = [] #lista con tutti i resti delle divisioni
quoziente = 1
while True:
    if num < 1 or quoziente < 1:
        break
    elif quoziente <= num:
        math.trunc(num)/ math.trunc(quoziente)
        quoziente = num / 2
        resto = math.trunc(num)%2
        binario.append(resto)
        num = quoziente
    else:
        math.trunc(num)/ math.trunc(quoziente)
        num = quoziente / 2
        resto = math.trunc(quoziente)%2
        binario.append(resto)
        quoziente = num

binario.reverse()
print(binario)

# controllo
bin = int(input("Puoi riscivere il numero binario che è risultato? "))
controllo = int(str(bin), base=2) #numero decimale
if n == controllo:
    print("Il programma funzionaaa!!")
    print("Il numero è", bin)
else:
    print("I numeri non coincidono, qualcosa è andato storto!")

# Ho cambiato la funzione round() con trunc() 
# Funziona perchè la funzione trunc() tronca tutta la parte decimale del numero e non lo approssima mai per eccesso
# Invece la funzione round() approssimava i numeri come "37.5" a "38" e questo genera un errore nel calcolo del resto