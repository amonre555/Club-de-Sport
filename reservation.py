from salle import Salle
from inscrit import Inscrit
from enums import TypeSalle, TypeForfait


class Reservation:
    def __init__(self, horaire: str, type_salle: TypeSalle, salle: Salle):
        self._horaire = horaire
        self._type = type_salle
        self._salle = salle

    def get_horaire(self):
        return self._horaire

    def set_horaire(self, horaire: str):
        self._horaire = horaire

    def get_type(self):
        return self._type

    def set_type(self, type_salle: TypeSalle):
        self._type = type_salle

    def get_salle(self):
        return self._salle

    def set_salle(self, salle: Salle):
        self._salle = salle

    def calculer_prix(self, inscrit: Inscrit):
        type_forfait = inscrit.get_forfait()
        type_salle = self.get_type()

        if type_forfait == TypeForfait.TICKET:
            if type_salle == TypeSalle.TENNIS:
                return 30.0
            elif type_salle == TypeSalle.BADMINTON:
                return 20.0
            elif type_salle == TypeSalle.SQUASH:
                return 15.0
        elif type_forfait == TypeForfait.FORFAIT:
            if type_salle == TypeSalle.TENNIS:
                return 11.0
            elif type_salle == TypeSalle.BADMINTON:
                return 10.0
            elif type_salle == TypeSalle.SQUASH:
                return 9.0

        return 0.0

    def traiter(self, inscrit: Inscrit):
        prix = self.calculer_prix(inscrit)
        salle_concernee = self.get_salle()

        if not salle_concernee.get_dispo():
            raise ValueError("La salle n'est pas disponible.")

        solde_actuel = inscrit.get_solde()
        if solde_actuel < prix:
            raise ValueError("Le solde de l'inscrit est insuffisant.")

        inscrit.set_solde(solde_actuel - prix)

        capacite_actuelle = salle_concernee.get_capacite()
        salle_concernee.set_capacite(capacite_actuelle - 1)

        liste_inscrits = salle_concernee.get_inscrits()
        liste_inscrits.append(inscrit)
        salle_concernee.set_inscrits(liste_inscrits)

        if salle_concernee.get_capacite() <= 0:
            salle_concernee.set_dispo(False)
