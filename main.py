# tabouret
"""
- hauteur
- couleur
- poid
=> se plier
=> se déplier
"""
# tabouret = {
#     "hauteur": None,
#     "couleur": None,
#     "poid": None,
#     "etat": "déplié"
# }
# def se_plier(tab):
#     tab["etat"] = "plié"
# def se_deplier(tab):
#     tab["etat"] = "déplié"

class Tabouret:
    # variables = attributs
    hauteur = 1
    couleur = "noir"
    poid = 1
    etat = "déplié"
    # fonctions = méthodes
    def se_plier(self):
        self.etat = "plié"
    def se_deplier(self):
        self.etat = "déplié"
    # méthode spéciale
    def __repr__(self):
        # REPResentation
        msg = (
            f'hauteur : {self.hauteur}\n'
            f'couleur : {self.couleur}\n'
            f'poid : {self.poid}\n'
            f'état : {self.etat}\n'
            f'--------------------\n'
        )
        return msg
    def __init__(self, hauteur = 1, couleur = "noir", poid = 1, etat = "déplié"):
        # constructeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.poid = poid
        self.etat = etat
        print("objet tabouret créé")
        print(hauteur, couleur, poid, etat)

t1 = Tabouret()
print(t1)
t2 = Tabouret(10, "bleu", 40, "plié")
print(t2)