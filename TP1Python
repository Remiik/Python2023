from datetime import date

#TP1, exercice 1
def age(annee_naissance):
    aujourd_hui = date.today()
    age_en_annees = aujourd_hui.year - annee_naissance
    age_en_mois = (aujourd_hui.year - annee_naissance) * 12 + aujourd_hui.month - 1
    age_en_jours = (aujourd_hui - date(annee_naissance, 1, 1)).days
    age_en_semaines = age_en_jours // 7
    print("Année de naissance : ", annee_naissance)
    print(f"Age en années : {age_en_annees}")
    print(f"Age en mois : {age_en_mois}")
    print(f"Age en jours : {age_en_jours}")
    print(f"Age en semaines : {age_en_semaines}")
# Exemple d'utilisation
age(1990)

#TP1, exercice 2
PhraseExemple = input("Saisir une phrase au hasard : ")
print("Taille de la phrase d'exemple: ", len(PhraseExemple))

#TP1, exercice 3 
CptVoyelles = len([char for char in PhraseExemple if char in "aeiouyAEIOUY"])

print("Nombre de voyelles: ", CptVoyelles)

#TP1, exercice 4
print("Nombre de caractères a : ", PhraseExemple.count('a'))

#TP1, exercice 5
TblMaListe = []
TblMaListe.append([PhraseExemple.split()])
print("Mots utilisés dans la phrase : ", TblMaListe)

#TP1, exercice 6, 7 & 8
MotAchercherDansListe = input("Saisir quelque chose à ajouter à la liste de mots précédemment affichée : ")

if MotAchercherDansListe in PhraseExemple:
    print(MotAchercherDansListe, "Est présent dans la liste de mots. On le supprime de la liste.")
    TblMaListe.pop(PhraseExemple.index(MotAchercherDansListe))
else:
    print(MotAchercherDansListe, "n\'est pas présent dans la liste de mots. On l'ajoute à la liste.")
    TblMaListe.append(MotAchercherDansListe)

#TP1, exercice 9 & 10

TableauOuStop = input("Voulez-vous voir le tableau en faisant écrivant \"tableau\" ou sortir en écrivant \"stop\" ?")

if TableauOuStop == "tableau":
    print(TblMaListe)
else:
    print("Input non-reconnu.")
