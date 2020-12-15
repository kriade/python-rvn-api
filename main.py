#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.splitter import Splitter
from lib.mfitzer import Mfitzer

import logging
import argparse
import sys

logger = logging.getLogger(__name__)

def parse_args(args=sys.argv[1:]):
    """Initialisation de la gestion des arguments CLI

    Args:
        args ([str], optional): Liste d'argument. Defaults to sys.argv[1:].

    Returns:
        [Namespace]: (command=str, destination=str, source=str)
    """
    parser = argparse.ArgumentParser(description='Commande relevé de notes')
    subparsers = parser.add_subparsers(help='sub-command help')

    add_load_subparser(subparsers)

    return parser.parse_args(args)


def add_load_subparser(subparsers):
    """Définition des arguments
    """
    parser = subparsers.add_parser('rvn', help='Application Relevé de Notes')
    parser.add_argument('-i', '--input', required=True, type=str,
                        help='Chemin des fichiers pdf à spliter')
    parser.add_argument('-o', '--output', required=True, type=str,
                        help='Chemin du dossier de destination des fichiers obtenues')
    parser.add_argument('-f', '--force', action='store_true',
                        help='Crée le répertoire de sortie si celui-ci n\'existe pas ')
    parser.add_argument('--debug', action='store_true', help='Active les taces logger')
    parser.set_defaults(command='rvn')


def main(inputpdf: str, outputdir: str, *, flag_join=True, flag_mkdir=False) -> None:
    """Fonction principale

    Args:
        inputpdf (str): Chemin du fichier pdf
        outputdir (str): Chemin de destination des fichiers pdf séparés
        flag_join (bool, optional): Si rvn est égal à True, alors le pdf traité est un
                                    pdf relevé de notes de l'universite de la Réunion.
                                    Sinon, c'est un fichier pdf quelconque.
                                    Defaults to True.
        flag_mkdir (bool, optional): Pour forcer la création du chemin de destination.
                                     Defaults to False.
    """
    spl = Splitter(inputpdf)
    mftiz = Mfitzer(outputdir)

    spl.split(outputdir, mkdirr=flag_mkdir)
    mftiz.mftzer_main(join=flag_join)


if __name__ == "__main__":

    # init args
    args = parse_args()

    # Récupération des arguments
    if args.command:
        source = args.input
        destination = args.output
        force = args.force
        if args.debug:
            # Debug
            logging.basicConfig(format='%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s', level=logging.DEBUG)

    # Exemple
    # source = 'test/RDN_GONOVA.pdf'
    # destination = 'test/tmppdf'

    main(source, destination, flag_mkdir=force)

    logger.info('Process was successfully completed')
    sys.exit(0)
