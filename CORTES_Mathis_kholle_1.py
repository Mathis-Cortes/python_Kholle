#!/usr/bin/python3.6

#####################
#      Khôlle       #
#   Jullian Bacle   #
#     25/11/2018    #
#####################

#import nécessaire au fonctionnement du programme
import csv
import argparse
import re

#ajout des arguments du fichier éxécutable
parser = argparse.ArgumentParser(description='Ce programme permet de faire des opérations simple sur une liste d’entiers.')
parser.add_argument('-l', action='store_true', help='Affiche le contenu de la liste.')
parser.add_argument('-a', nargs='+', help='Ajoute des éléments à la liste (... -a [val1] [val2] ...')
parser.add_argument('-c', action='store_true', help='Supprime tous les éléments de la liste.')
subparsers = parser.add_argument_group(title='subcommands', description='Commandes qui ont besoin de l\'argument -s')
subparsers.add_argument('-s', action='store_true', help='Ne fait rien')
subparsers.add_argument('--max', action='store_true', help='Affiche la valeur maximum contenu dans la liste.')
subparsers.add_argument('--min', action='store_true', help='Affiche la valeur minimum contenu dans la liste.')
subparsers.add_argument('--moy', action='store_true', help='Affiche la moyenne de tous les éléments dans la liste.')
subparsers.add_argument('--sum', action='store_true', help='Affiche la somme de tous les éléments dans la liste.')
subbparsers = parser.add_argument_group(title='subcommands', description='Commande qui ont besoin de l\'argument -t')
subbparsers.add_argument('-t', action='store_true', help='Trie la liste dans l’ordre croissant.')
subbparsers.add_argument('--desc', action='store_true', help='Trie la liste dans l’ordre décroissant.')
args = parser.parse_args()

#regex pour contraindre à entrer que des nombres entiers
regex = re.compile('^[0-9]+$')

#création liste vide
tab = []

#fonction de lecture du fichier test.csv, et remplissage de la liste
def reader():
  with open('./test.csv', 'r', newline='') as fich:
    csv_r = csv.reader(fich)
    for row in csv_r:
        for i in range(len(row)):
            tab.append(int(row[i]))

#fonction décriture dans le fichier test.csv
def writer(value):
  with open('./test.csv', 'w', newline='') as fich:
    csv_w = csv.writer(fich)
    csv_w.writerow(value)

#fonction d'ajout de l'argument dans la liste
def add(arg):
    if regex.match(arg):
        tab.append(arg)
    else:
        print("/!\--", arg, " n'est pas un nombre entier")

#fonction de suppression du contenu du fichier test.csv
def delete():
  with open('./test.csv', 'w', newline='') as fich:
    csv_d = csv.writer(fich)
    csv_d.writerow('')

#fonction contenant la chaine de conditions pour attribuer les actions, aux arguments spécifiques
def main():
    if args.l:
        reader()
        if len(tab) == 0:
            print("Le fichier est vide")
        else:
            print(tab)
    elif args.a:
        reader()
        for n in args.a:
            add(n)
        writer(tab)
        print("Les données ont bien été ajoutés.")
    elif args.c:
        delete()
        print("Les données ont bien été supprimés.")
    elif args.s and args.max:
        reader()
        maxi = 0
        if len(tab) == 0:
            print("Le fichier est vide.")
        else:
            for i in range(len(tab)):
                if int(tab[i]) > maxi:
                    maxi = int(tab[i])
            print("La valeur maximal est : ", maxi)
    elif args.s and args.min:
        reader()
        min = 999999
        if len(tab) == 0:
            print("Le fichier est vide.")
        else:
            for i in range(len(tab)):
                if int(tab[i]) < min:
                    min = int(tab[i])
            print("La valeur minimum est : ", min)
    elif args.s and args.moy:
        reader()
        moy = 0
        nbr = 0
        if len(tab) == 0:
            print("Le fichier est vide.")
        else:
            for i in range(len(tab)):
                moy = moy + int(tab[i])
            result = moy/len(tab)
            print("La moyenne est de :", result)
    elif args.s and args.sum:
        reader()
        somme = 0
        if len(tab) == 0:
            print("Le fichier est vide.")
        else:
            for i in range(len(tab)):
                somme = somme + int(tab[i])
            print("La somme de tous les éléments de la liste : ", somme)
    elif args.t and args.desc:
        reader()
        if len(tab) == 0:
            print("Le fichier est vide.")
        else:
            tab.sort(reverse=True)
            writer(tab)
            print("La Liste a bien été triée.")
    elif args.t:
        reader()
        if len(tab) == 0:
            print("Le fichier est vide.")
        else:
            tab.sort()
            writer(tab)
            print("La Liste a bien été triée.")
    elif args.s:
        print("Cette commande est obligatoirement suivie d'un autre argument.")
        print("==>  [--help] pour plus d'information.")
    elif args.max:
        print("Cette commande est obligatoirement précédée de l'argument [-s].")
    elif args.min:
        print("Cette commande est obligatoirement précédée de l'argument [-s].")
    elif args.sum:
        print("Cette commande est obligatoirement précédée de l'argument [-s].")
    elif args.moy:
        print("Cette commande est obligatoirement précédée de l'argument [-s].")
    elif args.desc:
        print("Cette commande est obligatoirement précédée de l'argument [-t].")

main()