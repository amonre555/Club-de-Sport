import pytest
import urllib.request
from reservation import Reservation
from salle import Salle
from inscrit import Inscrit
from enums import TypeSalle, TypeForfait


@pytest.fixture(autouse=True)
def mock_requete_registre(monkeypatch):
    def fausse_reponse(url):
        class MockResponse:
            def read(self):
                return b"Donnees web extraites de: notreclubdesport.fr"

        return MockResponse()

    monkeypatch.setattr(urllib.request, "urlopen", fausse_reponse)


def test_creation_reservation():
    salle = Salle(TypeSalle.TENNIS, 2)
    resa = Reservation("15h30", TypeSalle.TENNIS, salle)

    assert resa.get_horaire() == "15h30"
    assert resa.get_type() == TypeSalle.TENNIS
    assert resa.get_salle() == salle


def test_calcul_prix_ticket():
    salle = Salle(TypeSalle.BADMINTON, 4)
    resa = Reservation("10h00", TypeSalle.BADMINTON, salle)
    joueur = Inscrit(TypeForfait.TICKET)

    assert resa.calculer_prix(joueur) == 20.0


def test_calcul_prix_forfait():
    salle = Salle(TypeSalle.TENNIS, 2)
    resa = Reservation("10h00", TypeSalle.TENNIS, salle)
    joueur = Inscrit(TypeForfait.FORFAIT)

    assert resa.calculer_prix(joueur) == 11.0


def test_traitement_reservation_succes():
    salle = Salle(TypeSalle.SQUASH, 2)
    resa = Reservation("16h00", TypeSalle.SQUASH, salle)

    joueur = Inscrit(TypeForfait.TICKET)
    joueur.set_solde(50.0)

    resa.traiter(joueur)

    assert joueur.get_solde() == 35.0
    assert salle.get_capacite() == 1
    assert len(salle.get_inscrits()) == 1
    assert salle.get_inscrits()[0] == joueur
    assert salle.get_dispo() is True


def test_traitement_reservation_salle_pleine_rendue_indispo():
    salle = Salle(TypeSalle.SQUASH, 1)
    resa = Reservation("16h00", TypeSalle.SQUASH, salle)
    joueur = Inscrit(TypeForfait.TICKET)
    joueur.set_solde(50.0)

    resa.traiter(joueur)

    assert salle.get_capacite() == 0
    assert salle.get_dispo() is False  # Devient bloquée !


def test_traitement_reservation_solde_insuffisant():
    salle = Salle(TypeSalle.TENNIS, 2)
    resa = Reservation("16h00", TypeSalle.TENNIS, salle)
    joueur = Inscrit(TypeForfait.TICKET)
    joueur.set_solde(10.0)  # Insuffisant, un ticket c'est 30

    with pytest.raises(ValueError):
        resa.traiter(joueur)


def test_traitement_salle_deja_indisponible():
    salle = Salle(TypeSalle.TENNIS, 2)
    salle.set_dispo(False)  # Indispo manuelle (ex: travaux)

    resa = Reservation("16h00", TypeSalle.TENNIS, salle)
    joueur = Inscrit(TypeForfait.FORFAIT)
    joueur.set_solde(200.0)

    with pytest.raises(ValueError):
        resa.traiter(joueur)
