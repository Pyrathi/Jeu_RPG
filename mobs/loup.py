import arcade
import random
from personnages.entite_animee import EntiteAnimee
class Loup(EntiteAnimee):
    def __init__(self):
        super().__init__()
        self.textures = []
        for i in range(1, 4):
            texture = arcade.load_texture(f"images/mobs/loup_immobile{i}.png")
            self.textures.append(texture)
        self.texture = self.textures[0]
        self.scale = 0.5
        self.cur_texture_index = 0
        self.frame_count = 0
        self.center_x = 730
        self.center_y = 245
        
        
        
        
        
    
        #Stats
        self.sante = 25
        self.sante_max = 25
        self.mana = 0
        self.defense = 5
        
    def choix_attaque(self,cible):
        chifrre=random.random()
        if chifrre<=0.8:
            self.attaque_normale(cible)  
        else:
            self.attaque_lourde(cible)
        
    def attaque_normale(self, cible):
        degats = 15
        cible.recevoir_degats(degats)
        print(f"Le loup attaque et inflige {degats} points de dégâts. Santé restante de la cible : {cible.sante}")
    def attaque_lourde(self, cible):
        degats = 25
        cible.recevoir_degats(degats)
        print(f"Le loup utilise une attaque lourde et inflige {degats} points de dégâts. Santé restante de la cible : {cible.sante}")