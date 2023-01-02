import os
import json

dicEleves = { 
    'eleve1' : {'notes':{'tp1':10, 'tp2':13,'tp3':17}, 'appréciation': 'moyenne' }, 
    'eleve2' : {'notes' :{'tp1':19, 'tp2':11,'tp3':14}, 'appréciation': 'Très Bien' }, 
    'eleve3' : {'notes':{'tp1':15, 'tp2':8,'tp3':13}, 'appréciation': 'Bonne' }
}

# Création du dossier 'eleves' s'il n'existe pas déjà
if not os.path.exists('eleves'):
    os.mkdir('eleves')

# Création de dossiers pour chaque élève dans le dossier 'eleves'
for eleve in dicEleves:
    if not os.path.exists(f'eleves/{eleve}'):
        os.mkdir(f'eleves/{eleve}')

# Création du fichier 'appréciation.txt' dans chaque dossier d'élève
for eleve in dicEleves:
    with open(f'eleves/{eleve}/appréciation.txt', 'w') as f:
        f.write(dicEleves[eleve]['appréciation'])

# Création du fichier 'notes.csv' dans le dossier 'eleves'
for eleve in dicEleves:
    with open(f'eleves/{eleve}/notes.csv', 'w') as f:
        notes = dicEleves[eleve]['notes']
        f.write('TPs\n==================\n')
        f.write('TP1 : 'f'{notes["tp1"]}\n')
        f.write('TP2 : 'f'{notes["tp2"]}\n')
        f.write('TP3 : 'f'{notes["tp3"]}\n')

# Création du fichier 'eleves.json' dans le dossier 'eleves'
with open('eleves/eleves.json', 'w') as f:
    for eleve in dicEleves:
        json.dump(dicEleves[eleve], f)
