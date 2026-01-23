class arme(object):
    def __init__(self, nom, degats, rarete, texture=None):
        self.nom = nom
        self.degats = degats
        self.rarete = rarete
        self.texture = texture
        
class baton_base(arme):
    def __init__(self):
        super().__init__("Bâton de base", 5, "commun", texture="images/objets/mage/arme/baton_base.png")
        self.mana_cout_speciale = 30
    
    def attaque_speciale(self, cible):
        degats = 15
        cible.recevoir_degats(degats)
        

class baton_vide(arme):
    def __init__(self):
        super().__init__("Bâton du vide", 15, "légendaire", texture="images/objets/mage/arme/baton_vide.png")
        
        
class armure(object):
    def __init__(self, nom, defense, rarete, texture=None):
        self.nom = nom
        self.defense = defense
        self.rarete = rarete
        self.texture = texture
        
class robe_base(armure):
    def __init__(self):
        super().__init__("Robe de base", 10, "commun", texture="images/objets/mage/armure/robe_base.png")
        
class robe_enchantee(armure):
    def __init__(self):
        super().__init__("Robe enchantée", 20, "rare", texture="images/objets/mage/armure/robe_enchante.png")