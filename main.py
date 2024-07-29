class Hewan:
    def __init__(self, nama, spesies):
        self.nama = nama
        self.spesies = spesies

    def suara(self):
        pass

class Singa(Hewan):
    def __init__(self, nama, spesies):
        super().__init__(nama, spesies)

    def suara(self):
        return "Mengaum"

class Gajah(Hewan):
    def __init__(self, nama, spesies):
        super().__init__(nama, spesies)

    def suara(self):
        return "brrrr"
    
class Monyet(Hewan):
    def __init__(self, nama, spesies):
        super().__init__(nama, spesies)

    def suara(self):
        return "uu aa"

Singa = Singa("Simba", "Buas")
Gajah = Gajah("Artur", "Besar")
Monyet = Monyet("George", "Primata")

print(f"{Singa.nama} adalah Singa dengan spesias {Singa.spesies} dan memiliki suara {Singa.suara()}")
print(f"{Gajah.nama} adalah Gajah dengan spesies {Gajah.spesies} dan memiliki suara {Gajah.suara()}")
print(f"{Monyet.nama} adalah Monyet dengan spesies {Monyet.spesies} dan memiliki suara {Monyet.suara()}")
