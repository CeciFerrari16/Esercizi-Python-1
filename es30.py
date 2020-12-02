# Esercizio 30, convertire un numero binario in decimale
'''
Fornisci la rappresentazione in decimale di un numero binario.
All'inizio si richiede il numero di cifre di cui è composto il numero binario; 
si esegue poi una ripetizione che richiede le cifre del numero binario una a una a partire da destra 
e per ciascuna calcola il prodotto della cifra binaria per la potenza di 2 corrispondente alla 
posizione della cifra binaria e aggiunge al risultato alla somma; la ripetizione viene eseguita per 
il contatore che va dal valore zero al valore di lunghezza diminuito di uno. Confronta poi il risultato con 
il valore ottenuto dalla funzione predefinita del linguaggio per convertire un numero binario in decimale.
'''
counter = 0
val = [] # raccolgo i valori da sommare
num = int(input("Quante cifre ha il numero binario scelto? "))
print("Inserisci le cifre del numero binario a partire da destra ad una ad una...")

for n in range(num):
    c = int(input("Qual è la cifra? "))
    valore = (2**counter) * c
    val.append(valore)
    counter += 1

print("Il numero è", sum(val))

#adesso facciamo il controllo
binario = input("Qual è il numero binario di prima? ")
decimale = int(binario, base=2)
if sum(val) == decimale:
    print("Il mio programma funzionaaa!!")
    print("Il numero è", decimale)
else:
    print("I numeri non coincidono, qualcosa è andato storto!")