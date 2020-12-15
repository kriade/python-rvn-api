import fitz
import logging
from sys import exit
from pathlib import Path
from typing import List

logger = logging.getLogger(__name__)

class Splitter:
    """Dedicate to pdf file split
    """

    def __init__(self, filename: str):
        if Path(filename).is_file():
            self.pdf = fitz.open(filename)
            self.nbpages = self.nbpages()

    def nbpages(self) -> int:
        """Return number of page of a PyMuPDF file

        Returns:
            int: number of page
        """
        return self.pdf.pageCount

    def split(self, output_directory: str, *, const_namefile="document", mkdirr=False) -> None:
        """Split a PyMuPDF document into one page pdf and save them in a output directory

        Args:
            output_directory (str): Directory destination path
            const_namefile (str, optional): String pattern for output filename. Defaults to "document".
                                            Keyword-only
        """
        p = Path(output_directory)

        def build():
            for i in range(self.nbpages):
                dst = fitz.open()
                dst.insertPDF(self.pdf, from_page=i, to_page=i)

                # Build pathfile
                outfile = Path.cwd() / output_directory / f'{const_namefile}-{i:02d}.pdf'

                dst.save(outfile)
                logger.debug(f'File -- {outfile} -- was saved')

        if not(p.is_dir()):
            logger.debug(f'Path {output_directory} does not exist')
            if mkdirr:
                # Create directory
                p.mkdir(exist_ok=True, parents=True)
                logger.debug(f'Create path : {output_directory}')

                build()
            else:
                logger.error(f'Unable to create path {output_directory}')
                logger.info('An error has occurred. Python program will be quit')
                exit(1)
        else:
            build()

    def check_nb_opdf(self, directory: str, *, pattern="*.pdf") -> bool:
        """Check if number of page in origin pdf is equal of the number of pdf in specific directory

        Args:
            directory (str): Directory path
            pattern (str, optional): Extension file. Defaults to "*.pdf".
                                     Keyword-only
        Returns:
            bool: True --> pikepdf number pages is equal of number of pdf in specific directory
                  False --> pikepdf number pages is not equal of number of pdf in specific directory
        """
        if not(Path(directory).is_dir()):
            return False
        else:
            if self.nbpages == len(sorted(Path(directory).glob(pattern))):
                return True
        return False
