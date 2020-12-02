# Esercizio 28 , Gara studenti
''' Dato un elenco di studenti partecipanti a una gara sportiva di lancio del peso (nome utente, lancio ),
visualizza il valore del lancio del vincitore ( valore massimo)'''

indice = 0
studenti = ["Giacomo", "Gianmarco", "Gianluca", "Gianfranco", "Fausto", "Luigi"]
lancio = [1.2, 1.4, 1.9, 0.9, 2.0, 1.7]

while True:
    if indice == 6:
        break
    else:
        print(studenti[indice], lancio[indice])
        indice += 1

print("Il valore del lancio del vincitore è", max(lancio))

# oppure con i dizionari
'''
studenti = { 
    "Giacomo" : 1.2,
    "Gianmarco" : 1.4,
    "Gianluca" : 1.9,
    "Gianfranco" : 0.9,
    "Fausto" : 2.0,
    "Luigi" : 1.7
}
'''