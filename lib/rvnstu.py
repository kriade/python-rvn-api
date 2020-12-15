from re import compile
from typing import List

class Rvnstu:
    """Class 'Définie un étudiant via son relevé de note'
    """

    def __init__(self, msg):
        self.msg = msg
        self.idstudent = self.__numetu()

    def __msgtolist(self) -> List[str]:
        """Split the lines at line boundaries and return in array

        Returns:
            List [str]: msg in list
        """
        return self.msg.splitlines()

    def __numetu(self) -> str:
        """Get id student from text

        Returns:
            str: id student
        """
        item = self.__msgtolist()

        # regex : exactely 8 digits
        # match to the student number
        pattern = compile(r'\b\d{8}\b')
        idstudent = ""
        for index in range(len(item)):
            if pattern.match(item[index]):
                idstudent = item[index]
                break
        return idstudent
