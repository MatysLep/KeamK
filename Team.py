from ParticipantLevel import ParticipantLevel


class Team:
    def __init__(self, name, participants=None):
        """
        Initialise une nouvelle équipe.

        :param name (str): Le nom de l'équipe.
        :param participants (list[Participant], optional): Une liste de participants. Defaults to None.

        :return: None

        >>> team = Team("Avengers")
        >>> print(team)
        --- AVENGERS ---

        >>> participant1 = ParticipantLevel("Iron Man", 3)
        >>> participant2 = ParticipantLevel("Captain America", 5)
        >>> team_with_participants = Team("Justice League", [participant1, participant2])
        >>> print(team_with_participants)
        --- JUSTICE LEAGUE ---
        1/ name : Iron Man, level : 3
        2/ name : Captain America, level : 5
        """
        self._name = name
        if participants is None:
            self._participants = []
        else:
            self._participants = participants

    def __str__(self):
        """
        Retourne une chaîne de caractères représentant l'équipe et ses participants.

        :param: Aucun

        :return str: Une chaîne de caractères représentant l'équipe et ses participants.

        >>> team = Team("Avengers")
        >>> participant1 = ParticipantLevel("Iron Man", 3)
        >>> team.add_participant(participant)
        >>> print(team)
        --- AVENGERS ---
        1/ name : Iron Man, level : 3
        """
        res = "--- "+self._name.upper() + " ---"
        i = 0
        for participant in self._participants:
            i += 1
            res += "\n" + str(i) + "/ " + str(participant)
        return res

    def get_name(self):
        return self._name

    def add_participant(self, participant):
        """
        Ajoute un participant à l'équipe.

        :param participant: Le participant à ajouter.

        :return: None

        >>> team = Team("Avengers")
        >>> participant1 = ParticipantLevel("Iron Man", 3)
        >>> team.add_participant(participant)
        >>> print(team)
        --- AVENGERS ---
        1/ name : Iron Man, level : 3
        """
        self._participants.append(participant)

    def remove_participant(self, participant):
        """
        Supprime un participant de l'équipe.

        :param participant: Le participant à supprimer.

        :return: None

        >>> team = Team("Avengers")
        >>> participant1 = ParticipantLevel("Iron Man", 3)
        >>> team.add_participant(participant)
        >>> team.remove_participant(participant)
        >>> print(team)
        --- AVENGERS ---
        """
        self._participants.remove(participant)

    def get_participants(self):
        """
        Récupère la liste des participants de l'équipe.

        :param: Aucun

        :return list[Participant]: La liste des participants de l'équipe.

        >>> team = Team("Avengers")
        >>> participant = ParticipantLevel("Iron Man", 3)
        >>> team.add_participant(participant)
        >>> participants = team.get_participants()
        >>> participants[0].get_name()
        'Iron Man'
        """
        return self._participants

    def get_average(self):
        """
        Calcule le niveau moyen des participants de l'équipe.

        :param: Aucun

        :return float: Le niveau moyen des participants.
        """
        somme = 0
        n = 0
        for participant in self._participants:
            somme += participant.get_level()
            n += 1
        return somme / n if n > 0 else 0  # Evite la division par zéro
