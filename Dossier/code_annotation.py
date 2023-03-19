#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 11:01:56 2022

@author: Marina, Doruntina, Regina, Eirini
"""

import os # importation de la librairie pour manipuler des fichiers
import re # importation de la librairie des regex

def count_pos(fichier):
    file = open(fichier, "r", encoding="utf-8") # ouverture du fichier en mode lecture
    lignes = file.readlines() # lecture des lignes du fichier, et stockage dans une variable "lignes"
    pos = re.findall(" (ADJ|ADV|ART|PRP|PERS|PROP|PRON|KS|KC|DET|N|V|NUM|INDP NOM)(\W|\s)+", str(lignes)) # recherche des POS dans la variable lignes en string
    ''' # Pour vérifier au cas par cas :
    adj = re.findall(" ADJ", str(lignes))
    print("ADJ :", len(adj))
    adv = re.findall(" ADV", str(lignes))
    print("ADV :", len(adv))
    art = re.findall(" ART", str(lignes))
    print("ART :", len(art))
    prp = re.findall(" PRP", str(lignes))
    print("PRP :", len(prp))
    pers = re.findall(" PERS", str(lignes))
    print("PERS :", len(pers))
    prop = re.findall(" PROP", str(lignes))
    print("PROP :", len(prop))
    pron = re.findall(" PRON", str(lignes))
    print("PRON :", len(pron))
    ks = re.findall(" KS", str(lignes))
    print("KS :", len(ks))
    kc = re.findall(" KC", str(lignes))
    print("KC :", len(kc))
    det = re.findall(" DET", str(lignes))
    print("DET :", len(det))
    n = re.findall(" N\W+", str(lignes))
    print("N :", len(n))
    v = re.findall(" V ?", str(lignes))
    print("V :", len(v))
    num = re.findall(" NUM", str(lignes))
    print("NUM :", len(num))
    indp_nom = re.findall(" INDP NOM", str(lignes))
    print("INDP NOM :", len(indp_nom))
    #total = len(adj) + len(adv) + len(art) + len(prp) + len(pers) + len(prop) + len(pron) + len(ks) + len(kc) + len(det) + len(n) + len(v) + len(num) + len(indp_nom)
    '''
    file.close() # on ferme le fichier
    return len(pos) # return le nombre de match trouvé avec la regex correspondant au nombre de pos
# output : integer

'''
print("Annotations automatiques :")
print("Marina :", count_pos("anno_auto.txt")) # 283
print("Doruntina :", count_pos("Doruntina_Annotation_Automatique.txt")) # 294
print("Regina :", count_pos("a._automatiques_Regina.txt")) # 308
print("Eirini :", count_pos("annotations_auto_eirini.txt")) # 282
print()
print("Annotations manuelles :")
print("Marina :", count_pos("anno_manuelle.txt")) # 269
print("Doruntina :", count_pos("Doruntina_Aannotation_Manuelle.txt")) # 287
print("Regina :", count_pos("a._manuelle_regina.txt")) # 291
print("Eirini :", count_pos("annotations_manuelles_eirini.txt")) # 293
'''
print("Nombre de POS comptabilisés dans :")
print("L'annotation automatique :", count_pos("annotation_automatique_compile.txt"))
print("L'annotation manuelle :", count_pos("annotation_manuelle_compile.txt"))
print()

# fonction (qui marche), qui fait exactement la même chose que count_pos(), mais avec une regex iterateur
def recherche_pos(fichier): # 1 argument en entrée (un fichier)
    file = open(fichier, "r", encoding="utf-8") # ouverture du fichier en mode lecture
    lignes = file.readlines() # lecture des lignes du fichier, et stockage dans une variable "lignes"
    iterator = re.finditer(" (ADJ|ADV|ART|PRP|PERS|PROP|PRON|KS|KC|DET|N|V|NUM|INDP NOM)(\W|\s)+", str(lignes)) # recherche des POS dans la variable lignes en string
    count = 0 # création d'un compteur
    for match in iterator: # boucle qui tourne le nombre de fois de l'iterator
        count +=1 # j'incrémente mon compteur
    file.close() # on ferme le fichier
    return count # on retourne la valeur du compteur correspondant au nombre de POS
# output : integer

# fonction permettant de calculer la précision, le rappel et la F-mesure
def PRF(fichier1, fichier2, res): # 3 arguments : 2 fichiers, et le nombre de bons résultats trouvés (à rentrer manuellement)
    file1 = open(fichier1, "r", encoding="utf-8") # ouverture du fichier 1
    file2 = open(fichier2, "r", encoding="utf-8") # ouverture du fichier 2
    precision = res/count_pos(fichier2) # calcul de la precision avec le nbre rentré en argument et le résultat de la fonction count_pos sur le fichier 2
    print("La précision est de :", precision) # on print le résultat
    rappel = res/count_pos(fichier1) # calcul du rappel avec le nbre rentré en argument et le résultat de la fonction count_pos sur le fichier 1
    print("Le rappel est de :", rappel) # on print le résultat
    f_mesure = 2*(precision*rappel)/(precision+rappel) # formule de calcul de la F-mesure
    print("La F-mesure est de :", f_mesure) # on print le résultat
    file1.close() # on ferme le fichier 1
    file2.close() # on ferme le fichier 2

'''
print("Marina :")
PRF("anno_auto.txt","anno_manuelle.txt", 249)
print()
print("Doruntina :")
PRF("Doruntina_Annotation_Automatique.txt","Doruntina_Aannotation_Manuelle.txt", 273)
print()
print("Regina :")
PRF("a._automatiques_Regina.txt","a._manuelle_regina.txt", 260)
print()
print("Eirini :")
PRF("annotations_auto_eirini.txt","annotations_manuelles_eirini.txt", 274)
'''

PRF("annotation_automatique_compile.txt","annotation_manuelle_compile.txt", 1056)
print()

# fonction permettant de calculer le nombre de noms propres dans un fichier
def noms_propres(fichier): # 1 argument en entrée (un fichier)
    file = open(fichier, "r", encoding="utf-8") # ouverture du fichier en mode lecture
    lignes = file.readlines() # lecture des lignes du fichier, et stockage dans une variable "lignes"
    iterator = re.finditer(" PROP", str(lignes)) # recherche des noms propres dans la variable lignes en string
    count = 0 # création d'un compteur
    for match in iterator: # boucle qui tourne le nombre de fois de l'iterator
        count +=1 # j'incrémente mon compteur
    file.close() # on ferme le fichier
    return count # on retourne la valeur du compteur correspondant au nombre de noms propres
# output : integer

'''
print("Noms propres annotations automatiques :")
print("Marina :", noms_propres("anno_auto.txt"))
print("Doruntina :", noms_propres("Doruntina_Annotation_Automatique.txt"))
print("Regina :", noms_propres("a._automatiques_Regina.txt"))
print("Eirini :", noms_propres("annotations_auto_eirini.txt"))
print()
print()
print("Noms propres annotations manuelles :")
print("Marina :", noms_propres("anno_manuelle.txt"))
print("Doruntina :", noms_propres("Doruntina_Aannotation_Manuelle.txt"))
print("Regina :", noms_propres("a._manuelle_regina.txt"))
print("Eirini :", noms_propres("annotations_manuelles_eirini.txt"))
'''

print("Nombre de noms propres comptabilisés dans :")
print("L'annotation automatique :", noms_propres("annotation_automatique_compile.txt"))
print("L'annotation manuelle :", noms_propres("annotation_manuelle_compile.txt"))


