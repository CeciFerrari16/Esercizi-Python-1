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
num = int(input("Qual è il numero decimale da trasformare? "))
n = num
binario = [] #lista con tutti i resti delle divisioni
quoziente = 1
while True:
    if num == 0 or quoziente == 0:
        break
    elif quoziente <= num:
        quoziente = round(num / 2)
        resto = num%2
        binario.append(resto)
        num = quoziente
    else:
        num = round(quoziente / 2)
        resto = quoziente%2
        binario.append(resto)
        quoziente = num

binario.reverse()
print(binario)

# controllo
bin = int(input("Puoi riscivere il numero binario che è risultato? "))
controllo = int(str(bin), base=2) #numero decimale
print(controllo)
if n == controllo:
    print("Il programma funzionaaa!!")
    print("Il numero è", bin)
else:
    print("I numeri non coincidono, qualcosa è andato storto!")

# Nel provare ho notato che i numeri dal 290 in su sono sbagliati
# Probabilmente è dovuto ad errori di approssimazione