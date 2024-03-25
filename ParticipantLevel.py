from Participant import Participant


class ParticipantLevel(Participant):
    def __init__(self, name, level):
        """
                Initialise un nouveau participant avec un niveau.

                :param name (str): Le nom du participant.
                :param level (int): Le niveau du participant (entre 0 et 5).

                :return: None

                Exemple:
                >>> participant_level = ParticipantLevel("John Doe", 3)
        """
        self._level = level
        super().__init__(name)

    def __str__(self):
        """
                Retourne une chaîne de caractères représentant le participant et son niveau.

                :param: Aucun

                :return str: Une chaîne de caractères représentant le participant et son niveau.

                Exemple:
                >>> participant_level = ParticipantLevel("Jane Doe", 2)
                >>> print(participant_level)
                name : Jane Doe, level : 2
        """
        return super().__str__() + ", level : " + str(self._level)

    def get_level(self):
        """
        Récupère le niveau du participant.

        :param: Aucun

        :return int: Le niveau du participant (entre 0 et 5).

        >>> participant_level = ParticipantLevel("John Doe", 3)
        >>> level = participant_level.get_level()
        >>> level
        3
        """
        return self._level

    def set_level(self, level):
        """
                Modifie le niveau du participant.

                :param level: Le nouveau niveau du participant (entre 0 et 5).

                :return: None

                >>> participant_level = ParticipantLevel("John Doe", 3)
                >>> participant_level.set_level(2)
                >>> print(participant_level)
                name : John Doe, level : 2
        """
        while level < 0 or level > 5:
            print("Level must be between 0 and 5 \n")
            level = input("Level : ")
        self._level = level

    @staticmethod
    def create_participant():
        """
                Crée un nouveau participant avec un niveau en demandant son nom et son niveau à l'utilisateur.

                :param: Aucun

                :return ParticipantLevel: Un nouveau participant avec son niveau.

        """
        name = input("Enter your name: ")
        level = input("Level : ")

        if level < '0' or level > '5':
            raise ValueError("Level must be between 0 and 5 \n")

        return ParticipantLevel(name, int(level))
