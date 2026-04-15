import pytest
from salle import Salle
from enums import TypeSalle


def test_creation_salle():
    salle = Salle(TypeSalle.TENNIS, 2)
    assert salle.get_type() == TypeSalle.TENNIS
    assert salle.get_capacite() == 2
    assert salle.get_dispo() is True
    assert salle.get_inscrits() == []


def test_modification_type():
    salle = Salle(TypeSalle.TENNIS, 2)
    salle.set_type(TypeSalle.BADMINTON)
    assert salle.get_type() == TypeSalle.BADMINTON


def test_modification_capacite():
    salle = Salle(TypeSalle.TENNIS, 2)
    salle.set_capacite(4)
    assert salle.get_capacite() == 4


def test_modification_dispo():
    salle = Salle(TypeSalle.TENNIS, 2)
    salle.set_dispo(False)
    assert salle.get_dispo() is False


def test_modification_inscrits():
    salle = Salle(TypeSalle.TENNIS, 2)
    nouvelle_liste = ["Adherent1"]
    salle.set_inscrits(nouvelle_liste)
    assert salle.get_inscrits() == nouvelle_liste
