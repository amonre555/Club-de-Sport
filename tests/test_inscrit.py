import pytest
from inscrit import Inscrit
from enums import TypeForfait


def test_creation_inscrit():
    joueur = Inscrit(TypeForfait.TICKET)
    assert joueur.get_forfait() == TypeForfait.TICKET
    assert joueur.get_solde() == 0.0


def test_modification_forfait():
    joueur = Inscrit(TypeForfait.TICKET)
    joueur.set_forfait(TypeForfait.FORFAIT)
    assert joueur.get_forfait() == TypeForfait.FORFAIT


def test_modification_solde():
    joueur = Inscrit(TypeForfait.TICKET)
    joueur.set_solde(50.0)
    assert joueur.get_solde() == 50.0
