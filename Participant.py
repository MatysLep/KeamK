class Participant:
    def __init__(self, name):
        """
                Initialise un nouveau participant.

                :param name: Le nom du participant.

                :return: None

                Exemple:

                >>> participant = Participant("John Doe")
        """
        self._name = name

    def __str__(self):
        """
                La méthode permet de donner une représentation textuelle de l'instance de l'objet Participant.

                :param: Aucun

                :return str: Une chaîne de caractères représentant le participant.

                Exemple:

                >>> participant = Participant("John Doe")
                >>> print(participant)
                name : John Doe
                """
        return "name : " + self._name

    def get_name(self):
        """
                Récupère le nom du participant.

                :param: Aucun

                :return str: Le nom du participant.

                Exemple:

                >>> participant = Participant("John Doe")
                >>> name = participant.get_name()
                >>> print(name)
                John Doe
                """
        return self._name

    def set_name(self, name):
        """
                Modifie le nom du participant.

                :param name: Le nouveau nom du participant.

                :return: None

                Exemple:

                >>> participant = Participant("John Doe")
                >>> participant.set_name("Jane Doe")
                >>> print(participant)
                name : Jane Doe
                """
        self._name = name

    @staticmethod
    def create_participant():
        """
            Méthode statique

            Définition de la méthode:

            Crée un nouveau participant en demandant son nom à l'utilisateur.

            :param: Aucun

            :return Participant: Un nouveau participant.
        """
        return Participant(input("Name : "))
