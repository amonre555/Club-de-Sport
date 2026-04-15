from enums import TypeForfait


class Inscrit:
    def __init__(self, forfait: TypeForfait):
        self._forfait = forfait
        self._solde = 0.0

    def get_forfait(self):
        return self._forfait

    def set_forfait(self, forfait: TypeForfait):
        self._forfait = forfait

    def get_solde(self):
        return self._solde

    def set_solde(self, solde: float):
        self._solde = solde
