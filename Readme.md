# Flask Project

Ce projet est une application web développée avec Flask. Ce guide explique comment cloner le projet, installer les dépendances, configurer la base de données et lancer l'application.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- Python 3.x
- Pip (gestionnaire de paquets pour Python)
- Virtualenv (facultatif mais recommandé pour créer des environnements virtuels)
- Git

## Installation

### 1. Cloner le projet

Clonez le dépôt GitHub sur votre machine locale :

```bash
git clone https://github.com/soo-essoklina-ulrich/FLASKHOMEDATA.git
```

### 2. Créer un environnement virtuel

Créez un environnement virtuel pour isoler les dépendances du projet :

```bash
cd FLASKHOMEDATA
python -m venv venv
```

### 3. Activer l'environnement virtuel

Activez l'environnement virtuel :

- Sur Windows :

```bash
venv\Scripts\activate
```

- Sur macOS et Linux :

```bash
source venv/bin/activate
```

### 4. Installer les dépendances

Naviguez vers le répertoire du projet et installez les dépendances :

```bash
pip install -r requirements.txt
```

### 5. Configurer la base de données

Créez une base de données MySQL sur votre machine locale. Ensuite, créez un fichier `.env` à la racine du projet et ajoutez les informations de connexion à la base de données :

```bash
DATABASE_URL=mysql://<username>:<password>@localhost:3306/<database_name>
```

Creer les tables de la base de données en executant les commandes suivantes :

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6. Lancer l'application

Lancez l'application en exécutant la commande suivante :

```bash
flask run
```

L'application sera accessible à l'adresse `http://

## Auteur

- [Ulrich Essoklina](https://github.com/soo-essoklina-ulrich/)