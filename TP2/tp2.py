#!/usr/bin/env python3

"""Module d'introduction du TP2"""

auteur = "Mehdi Khelifi"

def copyright() :
    """Affiche le message de copyright"""
    print(auteur + " est l'unique auteur de ce programme, quiconque le copiera sans autorisation sera poursuivi par celui-ci")

def main() :
    print (auteur + " : ")
    copyright()

if __name__ == "__main__" :
    main()
