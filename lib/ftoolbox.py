from pathlib import Path
from typing import List

class Ftoolbox:
    """Class for file management
    """

    def get_pdffiles(self, directory_path: Path, *, extension='*.pdf') -> List:
        """Return path's file in array

        Args:
            directory_path (Path): Path directiory to analyze
            extension (str, optional): Extension file to search. Defaults to '*.pdf'.

        Returns:
            List: All file with extension in a array
        """
        p = directory_path.glob(extension)
        files = [x for x in p if x.is_file()]
        return files

    def remove_file(self, file: Path) -> None:
        """Remove a file

        Args:
            file (Path): Path file
        """
        Path.unlink(file)

    def rename_file(self, filename: Path, newbasename: str) -> None:
        """Rename an existing file

        Args:
            filename (Path): file to rename
            newbasename (str): new name for the file
        """
        if filename.is_file():
            old_name = filename.stem
            extension = filename.suffix
            directory = filename.parent
            new_name = newbasename + extension
            filename.rename(Path(directory, new_name))
