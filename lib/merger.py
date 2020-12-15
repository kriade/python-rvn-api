import fitz
from typing import List, Callable

class Merger:
    """Class use for merge pdf file
    """

    def merge(self, files: List, filepath: str, rmv: Callable[[str], None]) -> None:
        """Merge all fitz pdf file into one

        Args:
            files (List): List of all path pdf to merge
            filepath (str): Path directory to save the merged pdf
            rmv (Callable[[str], None]): Function to delete a pdf
        """
        dst = fitz.open()
        for file in files:
            dst.insertPDF(fitz.open(file))
            rmv(file)
        dst.save(filepath)
