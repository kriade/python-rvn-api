- [PDFTools](#pdftools)
  - [Prérequis](#prérequis)
  - [Installation Package](#installation-package)
  - [Utilisation](#utilisation)
    - [Arguments requis](#arguments-requis)
    - [Argument optionnel](#argument-optionnel)
    - [Dossier de destination](#dossier-de-destination)
  - [Template de référence](#template-de-référence)
    - [Relevé de notes aux semestres](#relevé-de-notes-aux-semestres)
    - [Relevé de notes à l'année](#relevé-de-notes-à-lannée)
  - [Librairie / Module](#librairie--module)
    - [PyMuPDF](#pymupdf)
    - [Argparse](#argparse)
  

# PDFTools

Ce script permet la création d'un fichier relevé de notes pour chaque étudiant par rapport à un fichier pdf relevé de notes extrait d'apogée.

## Prérequis

Les éléments suivants doivent être installé sur le serveur pour le bon fonctionnement du script python.
> - [Python 3](https://www.python.org/downloads/) (version 3.8 minimum)
> - Gestionnaire de package [PIP](https://pypi.org/project/pip/)

## Installation Package

L'ensemble des package requis pour le bon fonctionnement du script python est disponible dans le fichier [requirements.txt](requirements.txt).

La commande suivante installe les package répertoriés :
```sh
pip3 install -r requirements.txt
```

## Utilisation


L'exécution du script s'exécute via la commande suivante :
cru
```sh
./main.py rvn -i chemin/du/fichier.pdf -o chemin/du/dossier/destination
```

### Arguments requis

- `-i, --input` : path du fichier PDF relevé de note extraite d'Apogée.
- `-o, --output` : path du dossier qui accueillera les données extraites.

### Argument optionnel

- `-f, --force` : force la création du dossier de destination si celui si n'existe pas

### Dossier de destination

Le dossier de destination accueillera l'ensemble des fichiers PDF. Chaque PDF correspond à un relevé de notes d'un étudiant. 
Le nom du fichier PDF est formaté avec la nomenclature suivante :
`XXXXXXXX.pdf`
 
> - **XXXXXXXX** : Le numéro de l'étudiant.

## Template de référence

### Relevé de notes aux semestres

- Un exemple de fichier de fichier relevé de note extrait d'apogée est disponible dans le dossier [`docs/template_pdf/input/rvn_apogee.pdf`](docs/template_pdf/input/rvn_apogee.pdf).

- Un exemple d'extraction avec un relevé de note pour chaque étudiant est disponible dans le dossier [`docs/template_pdf/output/semestre`](docs/template_pdf/output/semestre).

- Un exemple d'extraction d'une page en text est disponible dans le fichier [`docs/template_pdf/template_message_referent.txt`](docs/template_pdf/template_message_referent.txt).  
Celui-ci a été extrait vie le module externe PyMuPDF de Python.  
Ce text est utilisé comme référentiel pour la recherche de donnée via des Regex.

### Relevé de notes à l'année

- Un exemple de fichier de fichier relevé de note extrait d'apogée est disponible dans le dossier [`docs/template_pdf/input/rvn_apogee_annee.pdf`](docs/template_pdf/input/rvn_apogee_annee.pdf).

- Un exemple d'extraction avec un relevé de note pour chaque étudiant est disponible dans le dossier [`docs/template_pdf/output/annee`](docs/template_pdf/output/annee).

- Un exemple d'extraction d'une page en text est disponible dans le fichier [`docs/template_pdf/template_message_2.txt`](docs/template_pdf/template_message_2.txt).  
Celui-ci a été extrait vie le module externe PyPDF2 de Python.  

## Librairie / Module

### PyMuPDF

Librairie pdf capable de splitter, fusionner et extraire les pages d'un fichier pdf.   
Documentation disponible sur : [`https://pymupdf.readthedocs.io/en/latest/`](https://pymupdf.readthedocs.io/en/latest/).

### Argparse

Gestion des options d'un script python pour l'exécution en ligne de commande.  
Documentation disponible sur : [`https://docs.python.org/3/library/argparse.html`](https://docs.python.org/3/library/argparse.html).

