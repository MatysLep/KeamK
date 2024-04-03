import random

from ParticipantLevel import ParticipantLevel
from SortBy import SortBy
from Team import Team


class Tirage:
    def __init__(self, name, nb_participants=0, nb_teams=0, participants=None, teams=None, sort=None):
        """
                Initialise un nouveau tirage.

                :param name (str): Le nom du tirage.
                :param nb_participants (int, optional): Le nombre de participants (défaut 0).
                :param nb_teams (int, optional): Le nombre d'équipes (défaut 0).
                :param participants (list[Participant], optional): Une liste de participants (défaut None).
                :param teams (list[Team], optional): Une liste d'équipes (défaut None).
                :param sort (SortBy, optional): Le type de tri à utiliser (défaut None).

                :return: None

                >>> tirage = Tirage("Test")
                >>> tirage._name
                'Test'
                >>> tirage._participants
                []
                >>> tirage._teams
                []
                >>> tirage._sortby is None
                True

                >>> tirage = Tirage("Tirage avec participants", participants=[ParticipantLevel("John Doe", 3)])
                >>> tirage._participants[0].get_name()
                'John Doe'

                >>> tirage = Tirage("Tirage avec équipes", teams=[Team("Avengers")])
                >>> tirage._teams[0].get_name()
                'Avengers'
                """
        if teams is None:
            teams = []
        if participants is None:
            participants = []
        self._name = name
        self._nb_participants = nb_participants
        self._nb_teams = nb_teams
        self._participants = participants
        self._teams = teams
        self._sortby = sort

    def set_nb_teams(self):
        """
               Définit le nombre d'équipes.

               :param: Aucun

               :return: None

            """
        n = input("Number of teams : ")
        while not n.isdigit() or int(n) < 1 or int(n) > int(self._nb_participants):
            if not n.isdigit():
                print(f"{n} is not a number.")
            else:
                print(f"{n} is not between 1 and {self._nb_participants}.")

            n = input("Enter a number: ")

        self._nb_teams = n

    @staticmethod
    def show_sort_by(enum):
        """
               Affiche les types de tri disponibles.

               :param enum: L'énumération contenant les types de tri.

               :return: None

                >>> tirage = Tirage("Tirage avec participants", participants=[ParticipantLevel("John Doe", 3)])
                >>> tirage.show_sort_by(SortBy)
                1 : NORMAL
                2 : GENDER
                3 : LEVEL
        """
        i = 0
        for member in enum:
            i += 1
            print(str(i) + " : " + member.name)

    def set_sort_by(self):
        """
               Définit le type de tri à utiliser.

               :param: Aucun

               :return: None
        """
        print(" Type of tirage ")
        Tirage.show_sort_by(SortBy)
        choice = '0'
        while choice < '1' or choice > '3':
            choice = input("choose a number between 1 et 3 : ")

        values = list(SortBy)
        self._sortby = values[int(choice) - 1]

    def set_nb_participants(self):
        """
               Définit le nombre de participants.

               :param: Aucun

               :return: None
               """
        n = input("Number of participants : ")
        while not n.isdigit():
            print(f"{n} is not a number.")
            n = input("Choose a number : ")
        self._nb_participants = n

    def __add_list_participant(self, participant):
        """
               Ajoute un participant à la liste des participants.

               :param participant: Le participant à ajouter.

               :return: None
        """
        self._participants.append(participant)

    def add_team(self):
        """
               Ajoute une équipe à la liste des équipes.

               :param: Aucun

               :return: None
        """
        self._teams.append(Team(input("name's team : ")))

    def add_all_participants(self):
        """
                Ajoute tous les participants en fonction du type de tri sélectionné.

                :param: Aucun

                :return: None

                #>>> tirage = Tirage("Test", sort=SortBy.NORMAL)  # Tirage normal
                #>>> tirage.set_nb_participants()  # Demande le nombre de participants via set_nb_participants
                #Number of participants : 3
                #>>> tirage._participants[0].get_name()  # Accède au premier participant créé
                #'John Doe'  # Le nom du participant peut varier
                #>>> tirage._participants[1].get_level()  # Accède au niveau du deuxième participant
                #3  # Le niveau du participant peut varier

                #>>> tirage = Tirage("Test", sort=SortBy.LEVEL)  # Tirage par niveau
                #>>> tirage.add_all_participants()
                #>>> tirage._participants[0].get_level() <= tirage._participants[1].get_level()
                #True  # Les participants sont triés par niveau croissant

                #>>> tirage = Tirage("Test", sort=SortBy.GENDER)  # Tirage par genre (supposant ParticipantGender)
                #>>> tirage.add_all_participants()
                # Les participants peuvent être triés par genre (M puis F)
                """
        self.set_nb_participants()
        for i in range(int(self._nb_participants)):
            try:
                self.__add_list_participant(self._sortby.value.create_participant())
            except ValueError as e:
                print(e)
                self.__add_list_participant(self._sortby.value.create_participant())

    def add_all_teams(self):
        """
                Ajoute le nombre défini d'équipes vides à la liste des équipes.

                :param: Aucun

                :return: None
        """
        self.set_nb_teams()
        for i in range(int(self._nb_teams)):
            self.add_team()

    def get_participants(self):
        """
                Affiche la liste des participants avec leur index.

                :param: Aucun

                :return: None

                >>> tirage = Tirage("Test")
                >>> tirage._participants = [ParticipantLevel("John Doe", 3), ParticipantLevel("Jane Doe", 2)]
                >>> tirage.get_participants()
                1, name : John Doe, level : 3
                2, name : Jane Doe, level : 2
        """

        i = 0
        for participant in self._participants:
            i += 1
            print(str(i) + ", " + str(participant))

    def show_teams(self):
        """
        Affiche la liste des équipes et leurs participants.

        :param: Aucun

        :return: None

        >>> tirage = Tirage("Test")
        >>> participant1 = ParticipantLevel("Alice", 2)
        >>> participant2 = ParticipantLevel("Bob", 5)
        >>> participant3 = ParticipantLevel("Marley", 1)
        >>> tirage._teams = [Team("Avengers", [participant1,participant3]), Team("Justice League", [participant2])]
        >>> tirage.show_teams()
        --- AVENGERS ---
        1/ name : Alice, level : 2
        2/ name : Marley, level : 1
        <BLANKLINE>
        --- JUSTICE LEAGUE ---
        1/ name : Bob, level : 5
        <BLANKLINE>
        """
        i = 0
        for team in self._teams:
            i += 1
            print(team.__str__() + "\n")

    def get_sortby(self):
        """
                Renvoie le type de tri utilisé par le tirage.

                :param: Aucun

                :return: Le type de tri (SortBy.NORMAL, SortBy.LEVEL, ou SortBy.GENDER).

                >>> tirage = Tirage("Test", sort=SortBy.NORMAL)
                >>> print(tirage.get_sortby())
                SortBy.NORMAL

                >>> tirage = Tirage("Test", sort=SortBy.LEVEL)
                >>> print(tirage.get_sortby())
                SortBy.LEVEL


        """
        return self._sortby

    def insert_participants_in_team(self):
        """
        Insère les participants dans les équipes en fonction du type de tri choisi.

        :param: Aucun

        :return: None
        """
        match self._sortby:
            case SortBy.NORMAL:
                self.insert_participants_normal_in_team()
            case SortBy.LEVEL:
                self.recursive_insert_participant_level_in_team()
            case _:
                self.insert_participants_gender_in_team()

    def insert_participants_normal_in_team(self):
        """
           Insère les participants dans les équipes de manière aléatoire.

           :param: Aucun

           :return: None

           >>> tirage = Tirage("Test")
           >>> participant1 = ParticipantLevel("Alice", 2)
           >>> participant2 = ParticipantLevel("Bob", 5)
           >>> participant3 = ParticipantLevel("Charlie", 3)
           >>> tirage._participants = [participant1, participant2, participant3]
           >>> team1 = Team('Avengers')
           >>> team2 = Team('Comics')
           >>> tirage._nb_teams = 2
           >>> tirage._teams = [team1, team2]  # Reset eams for clean test
           >>> tirage.insert_participants_normal_in_team()
           """
        list_participant = self._participants
        random.shuffle(list_participant)
        return self.recursive_insert_participants_in_team(list_participant, 0)

    def recursive_insert_participants_in_team(self, list_team, i):
        """
            Insère les participants restants dans les équipes de manière récursive.

            :param list_team: Une liste de participants restants à insérer.
            :param i: L'index de l'équipe en cours de remplissage.

            :return: None
        """
        if len(list_team) == 0:
            return
        else:
            self._teams[i % int(self._nb_teams)].add_participant(list_team.pop(0))
            return self.recursive_insert_participants_in_team(list_team, i + 1)

    def insert_participants_gender_in_team(self):
        """
                   Insère les participants avec un genre dans les équipes de manière aléatoire en équilibrant
                   le plus possible les genres dans chaque équipe.

                   :param: Aucun

                   :return: None
        """
        tab_f = self.team_per_gender('F')
        tab_m = self.team_per_gender('M')
        self.recursive_insert_participants_in_team(tab_f, 0)
        self.recursive_insert_participants_in_team(tab_m, 0)

    def insert_participants_level_in_team(self):
        """
                           Insère les participants avec un niveau dans les équipes de manière aléatoire en équilibrant
                           le plus possible les niveaux dans chaque équipe.

                           :param: Aucun

                           :return: None
                """
        list_sort = sorted(self._participants, key=lambda participant_level: participant_level.get_level())
        for i in range(int(self._nb_teams)):
            self._teams[i] = list_sort.pop(0)

    def recursive_insert_participant_level_in_team(self):
        """
            Insère les participants restants dans les équipes de manière récursive.

            :return: None
        """
        min_i = 0
        if len(self._participants) == 0:
            return 0
        else:
            for i in range(int(self._nb_teams)):
                if self._teams[i].get_average() < self._teams[min_i].get_average():
                    min_i = i
            self._teams[min_i].add_participant(self._participants.pop(0))
            return self.recursive_insert_participant_level_in_team()

    def team_per_gender(self, c):
        """ Trie un tableau de participants avec un genre et renvoie que les participants avec le genre égale
            au parametre 'c'
            :param c: 'M' ou 'F'
            :return: tab (list)
        """
        tab = []
        for participant in self._participants:
            if participant.get_gender() == c:
                tab.append(participant)
        return tab
