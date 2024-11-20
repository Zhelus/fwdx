from enum import Enum


class CollectionType(Enum):
    ACCOUNTS: str = 'Accounts'
    PATHOGENS: str = 'Pathogens'
    REAGENTS: str = 'Reagents'
    REPORTS: str = 'Reports'
    OLIGOS: str = 'Oligos'
