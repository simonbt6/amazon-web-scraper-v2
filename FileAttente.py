class Noeud:
    def __init__(self, d, s):  # Crée un nouveau noeud
        self.donnee = d
        self.suivant = s


class File:

    def __init__(self, max = None):
        self._arriere = None
        self._avant = None
        self._taille = 0
        self.max = max

    def taille(self):
        return self._taille

    def estvide(self):
        return self._taille == 0

    def premier(self) -> int:
        if self.estvide():
            raise LookupError('La file est vide')
        return self._avant.donnee

    def defile(self):
        if self.estvide():
            raise LookupError('La file est vide')
        item = self._avant.donnee
        self._avant = self._avant.suivant
        if self.estvide():
            self._arriere = None
        self._taille -= 1
        return item

    def enfile(self, s):
        nouveau = Noeud(s, None)
        
        if self.estvide():
            self._avant = nouveau
        elif self.full():
            return print("The queue is full")
        else:
            self._arriere.suivant = nouveau
        self._taille += 1
        self._arriere = nouveau
        

    def full(self):
        if self.max >= self.taille()+1 and self.max != None:
            return False
        return True
