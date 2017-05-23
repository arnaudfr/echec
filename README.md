# echec [![Build Status](https://travis-ci.org/arnaudfr/echec.svg?branch=master)](https://travis-ci.org/arnaudfr/echec) [![codecov](https://codecov.io/gh/arnaudfr/echec/branch/master/graph/badge.svg)](https://codecov.io/gh/arnaudfr/echec)
Projet ECHEC - Module Tests &amp; Recette

## Cahier de recette projet ECHEC

### Règles du jeu d’ECHEC:

* Echiquier : l’échiquier est un carré de taille variable, définie par l’utilisateur
* Joueurs : minimum 2, maximum 4, défini par l’utilisateur
* Pièces de jeu : créé par le joueur
* Déplacement pièces : une pièce se déplace selon un pattern défini par l’utilisateur


### Configuration partie:

* L’utilisateur choisi la taille de l’échiquier
* L’utilisateur choisi le nombre de joueurs (2-4)
* L’utilisateur choisi le budget alloué à chaque joueur
* Chaque joueur créé sa composition d’équipe avec son budget
    * Création des pièces
    * Placement des pièces 


### Création des pièces de jeu:

* Pattern de déplacement + jump feature* défini par le joueur
    * Jump feature : capacité pour une pièce à sauter par dessus d’autres pièces
* Coût d’une pièce : déterminé par la surface de déplacement potentiel maximale & jump feature

### Tests:

* Création grille de jeu (OK, trop grande, trop petite)
* Choix du nombre de joueurs (OK, trop élevé, trop faible)
* Choix du budget / joueur (OK, négatif)
* Création des pièces de jeu:
    * Création du pattern de déplacement (OK, déplacement max trop élevé, déplacement négatif)
    * Détermination du coût de la pièce (OK, négatif)
* Lancement partie (OK, echec)
* Déplacement pièce (OK, hors échiquier)
* Destruction pièce adverse (OK, échec)
* Resurrection pièce (OK, résurrection sans pion arrivé en bout d’échiquier = échec)
* Victoire (OK, destruction de toute les pièces)

