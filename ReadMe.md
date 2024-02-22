# Présentation
Ce programme a pour but la gestion de tournois d'échecs

# Instructions
## Prérequis
Avoir installé une version de Python égale ou supérieure à la 3.11.5

## Récupérer le programme

Téléchargement du dossier zip:
[en cliquant ici](https://github.com/marillierpeg/Openclassrooms_Projet-4/archive/refs/heads/main.zip)

Choisissez l'endroit où vous souhaitez le dézipper. C'est dans ce dossier que le programme stockera les fichiers extraits après lancement.

## Environnement virtuel
Principalement pour des raisons de compatibilité de versions et ainsi éviter tout bug du à des conflits de versions des librairies/packages utilisés, il est fortement conseillé de travailler au sein d'un environnement virtuel.

Commencez par utiliser votre terminal pour vous place dans le dossier que vous avez choisi pour dézipper.

#### Créer l'environnement virtuel

saisir la commande  suivante :
```
python -m venv env
```

#### Lancer l'environnement virtuel :

* saisir la commande  suivante  **sous Windows** (cmd) :
```
env\Scripts\activate.bat
```

* saisir la commande  suivante  **sous Windows** (PowerShell) :

```
env\Scripts\activate.ps1
```

* saisir la commande  suivante **sous Linux / Mac** :

```
source env/bin/activate
```

#### Installation des librairies/packages nécessaires :
```
pip install -r requirements.txt
```
Vous pouvez contrôler lesquels se sont installés avec la commande suivante : 
```
pip freeze
```


### Lancement des programmes
Saisir la commande suivante :
```
python3 main.py
```



## Vérification Flake8
Pour génrer un nouveau rapport attestant que le code de ce programme ne contient pas d'erreur et est conforme aux directives PEP 8, saisir la commande suivante :
```
flake8 --format=html --htmldir=flake8_rapport
```
