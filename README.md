# Projet_11_OpenClassrooms
## Améliorez une application Web Python par des tests et du débogage


###Description du projet :
Güdlft, une société qui a créé une plateforme numérique pour coordonner les compétitions de force 
(deadlifting, strongman) en Amérique du Nord et en Australie, a pour but:

- Analyse de performance d’une application avec Locust.
- Implémentation d'une suite de tests Python.
- Géstions des erreurs et les exceptions en Python.
- Ajout d'un Debug pour  le code de application Python.


### Récupérer le projet :

```
git clone https://github.com/ydjabela/Projet_11_Openclassrooms
```

### Création de l'environnement virtuel

Assurez-vous d'avoir installé python et de pouvoir y accéder via votre terminal, en ligne de commande.

Si ce n'est pas le cas : https://www.python.org/downloads/

```
python -m venv Projet_11
```

### Activation de l'environnement virtuel du projet

Windows :

```
Projet_11\Scripts\activate.bat
```

MacOS/Linux :
```
source Projet_11/bin/activate
```

### Installation des packages necessaire pour ce projet
```
pip install -r requirements.txt
```

### Fonctionnement:
Une fois activé, pour démarrer le serveur local, il faudra utiliser la commande :

Windows :
```
set FLASK_APP=server.py
flask run
```

MacOS/Linux :
```
export FLASK_APP=server.py
flask run
```
### Configuration actuelle

L'application est alimentée par [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). Il s'agit de contourner le fait d'avoir une base de données jusqu'à ce que nous en ayons réellement besoin. Les principaux sont :

* competitions.json - liste des compétitions
* clubs.json - liste des clubs avec des informations pertinentes. Vous pouvez regarder ici pour voir quelles adresses e-mail l'application acceptera pour la connexion.

### Tests

Vous êtes libre d'utiliser le framework de test que vous aimez, l'essentiel est que vous puissiez montrer les tests que vous utilisez.

Nous aimons aussi montrer à quel point nous testons bien, il y a donc un module appelé
[coverage](https://coverage.readthedocs.io/en/coverage-5.1/) que vous devez ajouter à votre projet.

Vous trouverez dans le dossier tests : des tests unitaires, fonctionnels et de performance, utilisant Pytest, Selenium et Locust.

ATTENTION : une fois exécutés, les tests Selenium nécessiteront un redémarrage du serveur local pour réussir (à améliorer).
* Tests unitaires:
```
cd test/unitaires
pytest
```
* Tests fonctionnels:
```
cd test/fonctionnels
python test_server.py
```
* Tests de performances:
Pour exécuter des tests de performances :
```
cd test/performances
locust
```
Interface web Locust disponible sur http://localhost:8089
#### Cette commande sera obligatoire à chaque fois que vous voudrez travailler avec le cours. Dans le même terminal, tapez maintenant
```
pip install -r requirements.txt
```
###Vérifier la qualité du code :
Pour lancer la vérification de la qualité du code : 
```
flake8 --format=html --htmldir=flake-report --exclude=env --max-line-length=119
```
### Contributeurs
- Yacine Djabela
- Stephane Didier
