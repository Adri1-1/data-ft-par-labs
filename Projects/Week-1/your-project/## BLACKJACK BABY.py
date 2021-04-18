## BLACKJACK BABY 


import random


valeur = { 'valeur' :  [2, 3, 4, 5, 6, 7, 8, 9, 10, 'R', 'D', 'V', 'A' ]}
couleur = { 'couleur' : ['carreau', 'coeur', 'trefle', 'pique'] }


# couleur = {'carreau' : [2, 3, 4, 5, 6, 7, 8, 9, 10,  'R', 'D', 'V', 'A' ],
#          'coeur' : [2, 3, 4, 5, 6, 7, 8, 9, 10, 'R', 'D', 'V', 'A' ],
#          'trefle' :[2, 3, 4, 5, 6, 7, 8, 9, 10, 'R', 'D', 'V', 'A' ],
#          'pique'  : [2, 3, 4, 5, 6, 7, 8, 9, 10,'R', 'D', 'V', 'A' ] }
continuer_partie = True
while continuer_partie:
    
    



def ma_carte(valeur, couleur):
    a = random.randrange(12)
    b = random.randrange(3)
    carte = (valeur['valeur'][a], couleur['couleur'][b])
    return carte


def mon_jeu(valeur, couleur):
    paquet = []
    for elt1 in valeur['valeur']:
        for elt2 in couleur['couleur']:
            paquet.append((elt1, elt2))
    return paquet
paquet = mon_jeu(valeur, couleur)

#print(paquet, len(paquet))
#fonction tirer un carte au hasard du paquet

def tirer_une_carte(set_):
    nbr= random.randrange(len(set_))
    new_carte = set_[nbr]
    set_.remove(new_carte)
    return new_carte

#print(carte_hasard)
#fonction qui mélange le paquet

def melange (lst):
    return random.sample(lst, k = len(lst))
    #return random.shuffle(lst)
new_paquet = melange(paquet)

#print(new_paquet, len(new_paquet))
#Fonction qui compare les cartes d une main

def calculer_valeur_une_main(cartes):
    val = 0
    for carte in cartes:
        if (carte[0] == 'R'):
            val += 10
        elif ( carte[0] == 'D'):
            val += 10
        elif (carte[0] == 'V'):
            val += 10
        elif 1 < carte[0] <= 10:
            val += carte[0]
    nb_as = cartes.count(1) # Attention s'il y a plusieurs as dans la main
    while nb_as>1:
        val += 1    # un seul as peut valoir 11 pts. Les autres valent 1.
        nb_as -= 1
    if nb_as == 1 and val + 11 <= 21:
        return val + 11
    elif 1 in cartes:
        return val + 1
    else:
        return val
    return val
# carte1 = ma_carte(valeur, couleur)
# carte2 = ma_carte(valeur, couleur)
carte1 = (1, 'trefle')
carte2 = (10, 'coeur')
carte3 = (10, 'coeur')
cartes = (carte1, carte2, carte3)
ma_valeur = calculer_valeur_une_main(cartes)
print(ma_valeur)