from enum import Enum

from Participant import Participant
from ParticipantGender import ParticipantGender
from ParticipantLevel import ParticipantLevel


class SortBy(Enum):
    NORMAL = Participant
    GENDER = ParticipantGender
    LEVEL = ParticipantLevel
