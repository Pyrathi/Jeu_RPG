class consomables():
    def __init__(self,nom,rarete,description,texture=None):
        self.nom = nom
        self.rarete = rarete
        self.texture = texture
        self.description = description

class potion_sante_petite(consomables):
    def __init__(self):
        super().__init__("Potion de santé petite","commun","Restaure 30 points de vie",texture="images/objets/potion_vie.png") 
        self.sante_restaurer=30
        