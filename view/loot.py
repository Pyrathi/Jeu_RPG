import arcade
from personnages.archer import Archer
from personnages.mage import Mage
from personnages.soldat import Soldat
from personnages.voleur import Voleur
from mobs.loup import Loup



# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "jeu"


class LootView(arcade.View):
    """View to show the loot of the game."""
    def __init__(self,personnage,loot,lieu_decor,mob):
        super().__init__()
        self.personnage=personnage
        self.loot=loot
        self.lieu_decor=lieu_decor
        self.background_color = arcade.csscolor.BEIGE
        self.mob=mob
        self.mob.preparer_visuel_mort()
        self.liste_personnages=arcade.SpriteList()
        self.personnage.center_x=520
        self.personnage.center_y=260
        self.liste_personnages.append(self.personnage)
        self.liste_mobs=arcade.SpriteList()
        self.liste_mobs.append(self.mob)
        #inventaire
        self.loot_table_texture=arcade.load_texture("images/UI/loot_table.png")
        self.loot_table_sprite=arcade.Sprite(self.loot_table_texture,scale=0.2)
        self.loot_table_sprite.center_x=WINDOW_WIDTH//2
        self.loot_table_sprite.center_y=500
        self.loot_table_sprite_list=arcade.SpriteList()
        self.loot_table_sprite_list.append(self.loot_table_sprite)
        
        #décor
        self.decor_texture=arcade.load_texture(self.lieu_decor)
        self.decor_sprite=arcade.Sprite(self.decor_texture,scale=0.7)
        self.decor_sprite.center_x=WINDOW_WIDTH//2
        self.decor_sprite.center_y=WINDOW_HEIGHT//2
        self.decor_sprite_list=arcade.SpriteList()
        self.decor_sprite_list.append(self.decor_sprite)
        
        #choix
        self.ui_loot_texture=arcade.load_texture("images/UI/equiper.png")
        self.ui_loot_sprite_equiper=arcade.Sprite(self.ui_loot_texture,scale=0.08)
        self.ui_loot_sprite_equiper.center_x=WINDOW_WIDTH//2 -100   
        self.ui_loot_sprite_equiper.center_y=350
        self.ui_loot_abandonner_texture=arcade.load_texture("images/UI/abandonner.png")
        self.ui_loot_sprite_abandonner=arcade.Sprite(self.ui_loot_abandonner_texture,scale=0.08)
        self.ui_loot_sprite_abandonner.center_x=WINDOW_WIDTH//2 +100    
        self.ui_loot_sprite_abandonner.center_y=350
        self.ui_loot_sprite_list=arcade.SpriteList()
        self.ui_loot_sprite_list.append(self.ui_loot_sprite_equiper)
        self.ui_loot_sprite_list.append(self.ui_loot_sprite_abandonner)
        
        self.ui_loot_unique_texture=arcade.load_texture("images/UI/loot_item_unique.png")
        self.ui_loot_unique_sprite=arcade.Sprite(self.ui_loot_unique_texture,scale=0.2)
        self.ui_loot_unique_sprite.center_x=WINDOW_WIDTH//2
        self.ui_loot_unique_sprite.center_y=500
        self.ui_prendre_texture=arcade.load_texture("images/UI/prendre.png")
        self.ui_prendre_sprite=arcade.Sprite(self.ui_prendre_texture,scale=0.1)
        self.ui_prendre_sprite.center_x=WINDOW_WIDTH//2 
        self.ui_prendre_sprite.center_y=350
        self.ui_loot_unique_sprite_list=arcade.SpriteList()
        self.ui_loot_unique_sprite_list.append(self.ui_loot_unique_sprite)
        self.ui_loot_unique_sprite_list.append(self.ui_prendre_sprite)

    def on_draw(self):
        self.clear()
        self.decor_sprite_list.draw()
        self.liste_personnages.draw()
        self.liste_mobs.draw()
        
        
        
        
        x_gauche = self.loot_table_sprite.center_x - 150
        y_haut = self.loot_table_sprite.center_y + 20
        if self.personnage.prochaine_arme is not None:
            arcade.draw_text(f"Vous avez ramassé un objet de rareté : {self.loot[0]}", 
                         WINDOW_WIDTH / 2, 
                         700,
                         arcade.color.BLACK, 
                         font_size=30, 
                         anchor_x="center", 
                         anchor_y="center")
            self.loot_table_sprite_list.draw()
            self.ui_loot_sprite_list.draw()
            self.loot_arme_sprite=arcade.Sprite(self.personnage.arme.texture,scale=0.05)
            self.loot_arme_sprite.center_x=x_gauche + 50
            self.loot_arme_sprite.center_y=y_haut + 13

            self.loot_prochaine_arme_sprite=arcade.Sprite(self.personnage.prochaine_arme.texture,scale=0.05)
            self.loot_prochaine_arme_sprite.center_x=x_gauche + 250
            self.loot_prochaine_arme_sprite.center_y=y_haut + 13
            self.loot_arme=arcade.SpriteList()
            self.loot_arme.append(self.loot_arme_sprite)
            self.loot_arme.append(self.loot_prochaine_arme_sprite)  
            self.loot_arme.draw()
            arcade.draw_text(self.personnage.arme.nom, 
                        x_gauche +20, y_haut-47, # x, y à ajuster selon ton image
                        arcade.color.BLACK, font_size=12)
            arcade.draw_text(f"Degats : {self.personnage.arme.degats}", 
                        x_gauche +20, y_haut-67, # x, y à ajuster selon ton image
                        arcade.color.BLACK, font_size=12)
            arcade.draw_text(f"Rareté : {self.personnage.arme.rarete}", 
                        x_gauche +20, y_haut-87, # x, y à ajuster selon ton image
                        arcade.color.BLACK, font_size=12)
            arcade.draw_text(self.personnage.prochaine_arme.nom, 
                        x_gauche +210, y_haut-47, # x, y à ajuster selon ton image
                        arcade.color.BLACK, font_size=12)
            arcade.draw_text(f"Degats : {self.personnage.prochaine_arme.degats}", 
                        x_gauche +200, y_haut-67, # x, y à ajuster selon ton image
                        arcade.color.BLACK, font_size=12)  
            arcade.draw_text(f"Rareté : {self.personnage.prochaine_arme.rarete}", 
                        x_gauche +200, y_haut-87, # x, y à ajuster selon ton image
                        arcade.color.BLACK, font_size=12)             
        elif self.personnage.prochaine_armure is not None:
            arcade.draw_text(f"Vous avez ramassé un objet de rareté : {self.loot[0]}", 
                         WINDOW_WIDTH / 2, 
                         700,
                         arcade.color.BLACK, 
                         font_size=30, 
                         anchor_x="center", 
                         anchor_y="center")
            self.loot_table_sprite_list.draw()
            self.ui_loot_sprite_list.draw()
            self.image_loot_sprite=arcade.Sprite(self.personnage.armure.texture,scale=0.05)
            self.image_loot_sprite.center_x=x_gauche + 50
            self.image_loot_sprite.center_y=y_haut +13
            self.image_prochaine_armure_sprite=arcade.Sprite(self.personnage.prochaine_armure.texture,scale=0.05)
            self.image_prochaine_armure_sprite.center_x=x_gauche + 250
            self.image_prochaine_armure_sprite.center_y=y_haut + 13
            self.image_loot=arcade.SpriteList()
            self.image_loot.append(self.image_loot_sprite)
            self.image_loot.append(self.image_prochaine_armure_sprite)
            self.image_loot.draw()
            arcade.draw_text(self.personnage.armure.nom, 
                        x_gauche +20, y_haut-47, # x, y à ajuster selon ton image
                        arcade.color.BLACK, font_size=12)
            arcade.draw_text(f"Défense : {self.personnage.armure.defense}", 
                        x_gauche +20, y_haut-67, # x, y à ajuster selon ton image
                        arcade.color.BLACK, font_size=12)
            arcade.draw_text(f"Rareté : {self.personnage.armure.rarete}", 
                        x_gauche +20, y_haut-87, # x, y à ajuster selon ton image
                        arcade.color.BLACK, font_size=12)
            arcade.draw_text(self.personnage.prochaine_armure.nom, 
                        x_gauche +220, y_haut-47, # x, y à ajuster selon ton image
                        arcade.color.BLACK, font_size=12)
            arcade.draw_text(f"Défense : {self.personnage.prochaine_armure.defense}", 
                        x_gauche +200, y_haut-67, # x, y à ajuster selon ton image
                        arcade.color.BLACK, font_size=12)  
            arcade.draw_text(f"Rareté : {self.personnage.prochaine_armure.rarete}", 
                        x_gauche +200, y_haut-87, # x, y à ajuster selon ton image
                        arcade.color.BLACK, font_size=12)
        elif self.loot[0]=="commun":
            arcade.draw_text(f"Vous avez ramassé un objet de rareté : {self.loot[0]}", 
                         WINDOW_WIDTH / 2, 
                         700,
                         arcade.color.BLACK, 
                         font_size=30, 
                         anchor_x="center", 
                         anchor_y="center")
            
            self.ui_loot_unique_sprite_list.draw()
            arcade.draw_text("Potion de soin", 
                        x_gauche +120, y_haut-65, # x, y à ajuster selon ton image
                        arcade.color.BLACK, font_size=12)
            arcade.draw_text(self.personnage.objet_recupere.description, 
                        x_gauche +80, y_haut-80, # x, y à ajuster selon ton image
                        arcade.color.BLACK, font_size=10)
            self.consommable_sprite=arcade.Sprite(self.personnage.objet_recupere.texture,scale=1.3)
            self.consommable_sprite.center_x=WINDOW_WIDTH//2
            self.consommable_sprite.center_y=500
            self.consommable_sprite_list=arcade.SpriteList()
            self.consommable_sprite_list.append(self.consommable_sprite)
            self.consommable_sprite_list.draw()
        elif self.loot[0]=="aucun":
            arcade.draw_text(f"Vous n'avez ramassé aucun objet.", 
                         WINDOW_WIDTH / 2, 
                         400,
                         arcade.color.BLACK, 
                         font_size=30, 
                         anchor_x="center", 
                         anchor_y="center")
            self.ui_continuer_texture=arcade.load_texture("images/UI/continuer.png")
            self.ui_continuer_sprite=arcade.Sprite(self.ui_continuer_texture,scale=0.1)
            self.ui_continuer_sprite.center_x=WINDOW_WIDTH//2
            self.ui_continuer_sprite.center_y=350
            self.ui_continuer_sprite_list=arcade.SpriteList()
            self.ui_continuer_sprite_list.append(self.ui_continuer_sprite)
            self.ui_continuer_sprite_list.draw()
        
        
    def on_key_press(self, key, modifiers):
    # C'est ici que nous vérifions quelle touche a été pressée
        if key==arcade.key.ESCAPE:
            self.window.set_fullscreen(False)
        if key==arcade.key.F5:
            from view.level import LevelView
            self.window.show_view(LevelView(self.personnage,self.lieu_decor,self.mob))
    
    def on_update(self, delta_time):
        self.liste_personnages.update()