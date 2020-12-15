import fitz
import logging

from pathlib import Path
from typing import List, Dict
from .rvnstu import Rvnstu
from .ftoolbox import Ftoolbox
from .merger import Merger

logger = logging.getLogger(__name__)

class Mfitzer:
    """Class object who add function to fitz module
    """

    def __init__(self, directory_path: str):
        self.directory_path = directory_path

    def readpage(self, file: str) -> str:
        """Return pdf first page to string

        Args:
            file (str): Fitz pdf

        Returns:
            str: text from pdf
        """
        doc = fitz.open(file)

        # First page
        page = doc[0]

        return page.getText()

    def data_idstudent(self, text: str) -> str:
        """Return id student from text (relevedenote)

        Args:
            text (str): text from pdf file

        Returns:
            str: id student
        """
        return Rvnstu(text).idstudent

    def joinpdf(self, data: List, mg: Merger, ft: Ftoolbox) -> None:
        """Merge pdf with same id student in name file

        Args:
            data (List): Array of id student
            mg (Merger): Object Merger
            ft (Ftoolbox): Object Ftoolbox
        """

        for id in data:
            pages = ft.get_pdffiles(Path(self.directory_path), extension=f'*{id}.pdf')
            mg.merge(pages, Path(self.directory_path, f'{id}.pdf'), ft.remove_file)

    def mftzer_main(self, *, join=False) -> Dict:
        """Rename file if pdf text have id student.
            Return dictionnary with {id_student, associated file number}

        Args:
            join (bool, optional): Flag for use joinpdf function or not. Default to False
                                   Keyword-only
        Returns:
            Dict: {id_student, associated file number}
        """
        # init object
        ft = Ftoolbox()

        # init result
        data = {}

        # all pdf files
        files = ft.get_pdffiles(Path(self.directory_path))

        for file in files:
            text = self.readpage(file)
            print(text)
            ne = self.data_idstudent(text)
            if ne:
                if ne not in data:
                    data[ne] = 1
                    ft.rename_file(file, ne)
                    logger.debug(f'{file} was renamed in {ne}.pdf')
                else:
                    data[ne] += 1

                    # formate name file
                    # "{int}-{id_student}"
                    newfilename = f'{data.get(ne)}-{ne}'

                    ft.rename_file(file, newfilename)
                    logger.debug(f'File already exists for id : {ne}')
                    logger.debug(f'New file name for save {newfilename}')

            else:
                # remove file who haven't student id
                ft.remove_file(file)
                logger.debug(f'File {file} was removed')

        # if value in dict > 1, return associated key in a list
        # and if flag join is equal True boolean
        if (karray := [a for a, b in data.items() if b > 1]) and (join):

            # init object
            mg = Merger()

            logger.debug('Join file with same id')
            self.joinpdf(karray, mg, ft)
