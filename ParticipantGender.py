from Participant import Participant


class ParticipantGender(Participant):
    def __init__(self, name, gender):
        """
        Initialise un nouveau participant avec un genre.

        :param name (str): Le nom du participant.
        :param gender (str): Le genre du participant ("M" ou "F").

        :return: None

        >>> participant_gender = ParticipantGender("John Doe", "M")
        """
        self._gender = gender
        super().__init__(name)

    def __str__(self):
        """
        Retourne une chaîne de caractères représentant le participant et son genre.

        :param: Aucun

        :return str: Une chaîne de caractères représentant le participant et son genre.

        >>> participant_gender = ParticipantGender("Jane Doe", "F")
        >>> print(participant_gender)
        name : Jane Doe, gender : F
        """
        return super().__str__() + ", gender : " + self._gender

    def get_gender(self):
        """
        Récupère le genre du participant.

        :param: Aucun

        :return str: Le genre du participant ("M" ou "F").

        >>> participant_gender = ParticipantGender("John Doe", "M")
        >>> gender = participant_gender.get_gender()
        >>> gender
        'M'
        """
        return self._gender

    def set_gender(self, gender):
        """
        Modifie le genre du participant.

        :param gender: Le nouveau genre du participant ("M" ou "F").

        :return: None

        >>> participant_gender = ParticipantGender("John Doe", "M")
        >>> participant_gender.set_gender("F")
        >>> print(participant_gender)
        name : John Doe, gender : F

        >>> participant_gender.set_gender("X")
        Traceback (most recent call last):
          ...
        ValueError: Le genre doit être M ou F
        """
        if gender not in ("M", "F"):
            raise ValueError("Le genre doit être M ou F")
        self._gender = gender

    @staticmethod
    def create_participant():
        """
        Crée un nouveau participant avec un genre en demandant son nom et son genre à l'utilisateur.

        :param: None

        :return ParticipantGender: Un nouveau participant avec son genre.
        """

        name = input("Enter your name: ")
        gender = input("Gender (M or F): ")

        if gender not in ("M", "F"):
            raise ValueError("Gender must be M or F\n")

        return ParticipantGender(name, gender)
