from enums import TypeSalle


class Salle:
    def __init__(self, type_salle: TypeSalle, capacite: int):
        self._type = type_salle
        self._capacite = capacite
        self._dispo = True
        self._inscrits = []

    def get_type(self):
        return self._type

    def set_type(self, type_salle: TypeSalle):
        self._type = type_salle

    def get_capacite(self):
        return self._capacite

    def set_capacite(self, capacite: int):
        self._capacite = capacite

    def get_dispo(self):
        return self._dispo

    def set_dispo(self, dispo: bool):
        self._dispo = dispo

    def get_inscrits(self):
        return self._inscrits

    def set_inscrits(self, inscrits: list):
        self._inscrits = inscrits
