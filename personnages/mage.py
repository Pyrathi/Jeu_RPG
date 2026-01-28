import arcade
import random
from items.mage_item import *
from personnages.entite_animee import EntiteAnimee
from items.objet import *
class Mage(EntiteAnimee):
    def __init__(self):
        super().__init__()
        self.textures = []
        for i in range(1, 5):
            texture = arcade.load_texture(f"images/mage/immobile/mage_immobile{i}.png")
            self.textures.append(texture)
        self.texture = self.textures[0]
        self.scale = 0.3
        self.cur_texture_index = 0
        self.frame_count = 0
        self.center_x = 250
        self.center_y = 500
        #UI
        self.ui_mage_texture=arcade.load_texture("images/mage/UI/Banner_Horizontal.png")
        self.ui_mage_sprite=arcade.Sprite(self.ui_mage_texture,scale=0.5)
        self.ui_mage_sprite.center_x=250
        self.ui_mage_sprite.center_y=600
        self.bouton_choisir_texture=arcade.load_texture("images/UI/choisir1.png")
        self.bouton_choisir_sprite=arcade.Sprite(self.bouton_choisir_texture,scale=0.5)
        self.bouton_choisir_sprite.center_x=395
        self.bouton_choisir_sprite.center_y=450
        
        
        #Description
        self.description_mage_texture=arcade.load_texture("images/mage/UI/fenetre_description.png")
        self.fenetre_stats=arcade.Sprite(self.description_mage_texture,scale=0.8)
        self.fenetre_stats.center_x=450     
        self.fenetre_stats.center_y=400
    
        #Stats
        self.sante = 50 
        self.sante_max = 50
        self.mana = 100
        self.mana_max = 100
        self.defense = 10
        
        self.arme=baton_base()
        self.prochaine_arme=None
        self.armure=robe_base()
        self.prochaine_armure=None
        self.objet_recupere=None
        self.inventaire = []
        
    def attaque_normale(self, cible):
        if self.mana < 15:
            print("Pas assez de mana pour attaquer.")
            
        else:
            degats = self.arme.degats
            self.mana -= 15
            if self.mana < 0:
                self.mana = 0
            cible.recevoir_degats(degats)
            if cible.sante < 0:
                cible.sante = 0
                cible.drop_loot(self)
            if cible.sante > 0:
                cible.choix_attaque(self)
            print(f"Le mage attaque et inflige {degats} points de dégâts. Santé restante de la cible : {cible.sante}")
        
    def meditation(self):
        mana_recuperee = 25
        self.mana = min(self.mana + mana_recuperee, self.mana_max)
        print(f"Le mage médite et récupère {mana_recuperee} points de mana. Mana actuelle : {self.mana}")
        
    def rammasser_loot(self, loot):
        self.prochaine_arme=None
        self.prochaine_armure=None
        self.objet_recupere=None
        print(f"Le mage ramasse un objet de rareté : {loot}")
        if loot[0] == "légendaire":
            self.prochaine_arme=loot[1]
            
        elif loot[0] == "rare":
            self.prochaine_armure=loot[1]
        elif loot[0] == "commun":
            print("Objet commun ramassé, pas d'amélioration.")
            self.objet_recupere=loot[1]
        else:
            print("Rien à ramasser.")
    
    def attaque_spéciale(self, cible):
        if self.mana >= self.arme.mana_cout_speciale:
            self.mana -= self.arme.mana_cout_speciale
            self.arme.attaque_speciale(cible)
            if cible.sante < 0:
                cible.sante = 0
                cible.drop_loot(self)
            if cible.sante > 0:
                cible.choix_attaque(self)
            
        else:
            print("Pas assez de mana pour l'attaque spéciale.")
        