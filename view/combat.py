import arcade
from personnages.archer import Archer
from personnages.mage import Mage
from personnages.soldat import Soldat
from personnages.voleur import Voleur
from mobs.loup import Loup
from view.loot import LootView


# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "jeu"

class CombatView(arcade.View):
    """View to show the combat of the game."""
    def __init__(self,personnage,lieu_decor,mob):
        super().__init__()
        self.personnage=personnage
        # Initialisation du niveau
        self.background_color = arcade.csscolor.BEIGE
        self.liste_personnages=arcade.SpriteList()
        self.personnage.center_x=520
        self.personnage.center_y=260
        self.liste_personnages.append(self.personnage)
        self.liste_mobs=arcade.SpriteList()
        self.mob=mob
        self.lieu_decor=lieu_decor
        self.liste_mobs.append(self.mob)
        self.ui_combat_texture1=arcade.load_texture("images/mage/UI/attack.png")
        self.ui_combat_sprite1=arcade.Sprite(self.ui_combat_texture1,scale=1.5)
        self.ui_combat_sprite1.center_x=500
        self.ui_combat_sprite1.center_y=50
        self.ui_combat_texture2=arcade.load_texture("images/mage/UI/attack.png")
        self.ui_combat_sprite2=arcade.Sprite(self.ui_combat_texture2,scale=1.5)
        self.ui_combat_sprite2.center_x=800
        self.ui_combat_sprite2.center_y=50
        self.ui_combat_texture3=arcade.load_texture("images/mage/UI/attack.png")
        self.ui_combat_sprite3=arcade.Sprite(self.ui_combat_texture3,scale=1.5)
        self.ui_combat_sprite3.center_x=500 
        self.ui_combat_sprite3.center_y=150
        self.ui_combat_texture4=arcade.load_texture("images/mage/UI/attack.png")
        self.ui_combat_sprite4=arcade.Sprite(self.ui_combat_texture4,scale=1.5)
        self.ui_combat_sprite4.center_x=800 
        self.ui_combat_sprite4.center_y=150
        self.ui_combat_list=arcade.SpriteList()
        self.ui_combat_list.append(self.ui_combat_sprite1)
        self.ui_combat_list.append(self.ui_combat_sprite2)
        self.ui_combat_list.append(self.ui_combat_sprite3)
        self.ui_combat_list.append(self.ui_combat_sprite4)

        #décor
        self.decor_texture=arcade.load_texture(self.lieu_decor)
        self.decor_sprite=arcade.Sprite(self.decor_texture,scale=0.7)
        self.decor_sprite.center_x=WINDOW_WIDTH//2
        self.decor_sprite.center_y=WINDOW_HEIGHT//2
        self.decor_sprite_list=arcade.SpriteList()
        self.decor_sprite_list.append(self.decor_sprite)
        #barre de vie
        self.LARGEUR_BARRE = 100
        self.barre_x = self.personnage.center_x - self.LARGEUR_BARRE // 2 - 20
        self.barre_y = self.personnage.center_y + 50
        self.mob_barre_x = self.mob.center_x - self.LARGEUR_BARRE // 2 - 20
        self.mob_barre_y = self.mob.center_y + 70
        
        #état de survol
        self.survol_vie_heros = False
        self.survol_vie_mob = False
        self.survol_mana_heros = False

    def on_update(self, delta_time):
        self.liste_personnages.update()
        self.liste_mobs.update()
   
    def on_draw(self):
        self.clear()
        self.decor_sprite_list.draw()
        self.liste_personnages.draw()
        self.liste_mobs.draw()
        self.ui_combat_list.draw()
        
        
        # --- Paramètres de la barre ---
        LARGEUR_TOTALE = 100
        HAUTEUR = 12
        arcade.draw_lbwh_rectangle_filled(self.barre_x, self.barre_y, self.LARGEUR_BARRE, HAUTEUR, arcade.color.BLACK)
        ratio_vie = self.personnage.sante / self.personnage.sante_max
        largeur_vie_actuelle = LARGEUR_TOTALE * ratio_vie
        bord_gauche = self.barre_x - (LARGEUR_TOTALE / 2)
        arcade.draw_lbwh_rectangle_filled(self.barre_x, self.barre_y, 
                                    largeur_vie_actuelle, HAUTEUR, arcade.color.GREEN)
        # Barre de vie du mob
        arcade.draw_lbwh_rectangle_filled(self.mob_barre_x, self.mob_barre_y, self.LARGEUR_BARRE, 10, arcade.color.BLACK)
        ratio_vie_mob = self.mob.sante / self.mob.sante_max
        largeur_vie_actuelle_mob = LARGEUR_TOTALE * ratio_vie_mob
        bord_gauche_mob = self.mob_barre_x - (LARGEUR_TOTALE / 2)
        arcade.draw_lbwh_rectangle_filled(self.mob_barre_x, self.mob_barre_y, 
                                    largeur_vie_actuelle_mob, HAUTEUR, arcade.color.RED)
                                    
        # Barre de mana
        if self.personnage.mana > 0:
            HAUTEUR_MANA = 8
            
            barre_mana_y = self.personnage.center_y + 70
            arcade.draw_lbwh_rectangle_filled(self.barre_x, barre_mana_y, self.LARGEUR_BARRE, HAUTEUR_MANA, arcade.color.BLACK)
            ratio_mana = self.personnage.mana / self.personnage.mana_max
            largeur_mana_actuelle = LARGEUR_TOTALE * ratio_mana
            arcade.draw_lbwh_rectangle_filled(self.barre_x, barre_mana_y, 
                                        largeur_mana_actuelle, HAUTEUR_MANA, arcade.color.BLUE)
        
        # Nom attaques
        arcade.draw_text(f"Attaque normale", 
                        self.ui_combat_sprite3.center_x, 
                        self.ui_combat_sprite3.center_y,
                        arcade.color.BLACK, 
                        font_size=15, 
                        anchor_x="center", 
                        anchor_y="center")
        if isinstance(self.personnage, Mage):
            arcade.draw_text("méditaion", 
                        self.ui_combat_sprite1.center_x, 
                        self.ui_combat_sprite1.center_y,
                        arcade.color.BLACK, 
                        font_size=15, 
                        anchor_x="center", 
                        anchor_y="center")
                        
        arcade.draw_text("Attaque spéciale", 
                        self.ui_combat_sprite4.center_x,
                        self.ui_combat_sprite4.center_y,
                        arcade.color.BLACK,
                        font_size=15,
                        anchor_x="center",
                        anchor_y="center")
        # Infos survol
        
        if self.survol_vie_heros:
            # Afficher la santé actuelle et maximale
            arcade.draw_text(f" {self.personnage.sante} / {self.personnage.sante_max}",
            	self.barre_x + 75,
            	self.barre_y + 8,
            	arcade.color.WHITE,
            	font_size=10,
            	anchor_x="center",
            	anchor_y="center"
            )
        if self.survol_mana_heros:
            # Afficher le mana actuelle et maximale
            arcade.draw_text(f" {self.personnage.mana} / {self.personnage.mana_max}",
            	self.barre_x + 70,
            	self.personnage.center_y + 75,
            	arcade.color.WHITE,
            	font_size=10,
            	anchor_x="center",
            	anchor_y="center"
            )
        if self.survol_vie_mob:
            # Afficher la santé actuelle et maximale du mob
            arcade.draw_text(f" {self.mob.sante} / {self.mob.sante_max}",
            	self.mob_barre_x +75,
            	self.mob_barre_y + 8,
            	arcade.color.WHITE,
            	font_size=10,
            	anchor_x="center",
            	anchor_y="center"
            )
                        
    
    def on_mouse_press(self, x, y, button, modifiers):
        for choix in self.ui_combat_list:
    	    if choix.collides_with_point((x, y)):
                if choix==self.ui_combat_sprite3:
                    if hasattr(self.personnage, 'attaque_normale'):
                        self.personnage.attaque_normale(self.mob)
                        print(f"Santé du mob après attaque : {self.mob.sante}")
                        if self.mob.sante <= 0:
                            print("Le mob est vaincu !")
                            loot=self.mob.drop_loot(self.personnage)
                            loot_view=LootView(self.personnage,loot,self.lieu_decor,self.mob)
                            self.window.show_view(loot_view)
                            
                elif choix==self.ui_combat_sprite1 and isinstance(self.personnage, Mage):
                    if hasattr(self.personnage, 'meditation'):
                        self.personnage.meditation()
                        print(f"Mana du personnage après méditation : {self.personnage.mana}")
                elif choix==self.ui_combat_sprite4:
                    if hasattr(self.personnage, 'attaque_spéciale'):
                        self.personnage.attaque_spéciale(self.mob)
                        print(f"Santé du mob après attaque spéciale : {self.mob.sante}")
                        if self.mob.sante <= 0:
                            print("Le mob est vaincu !")
                            loot=self.mob.drop_loot(self.personnage)
                            loot_view=LootView(self.personnage,loot,self.lieu_decor,self.mob)
                            self.window.show_view(loot_view)
        
    def on_mouse_motion(self, x, y, dx, dy):
        self.survol_mana_heros=False
        self.survol_vie_heros=False
        self.survol_vie_mob=False
        if x>self.barre_x and x<self.barre_x+self.LARGEUR_BARRE and y>self.barre_y and y<self.barre_y+12:
            # Afficher la santé actuelle et maximale
            self.survol_vie_heros = True
            
        elif x>self.mob_barre_x and x<self.mob_barre_x+self.LARGEUR_BARRE and y>self.mob_barre_y and y<self.mob_barre_y+12:
            # Afficher la santé actuelle et maximale du mob
            self.survol_vie_mob = True
            
        elif x>self.barre_x and x<self.barre_x+self.LARGEUR_BARRE and y>self.personnage.center_y+70 and y<self.personnage.center_y+78:
            # Afficher le mana actuelle et maximale
            self.survol_mana_heros = True
            



    def on_key_press(self, key, modifiers):
    # C'est ici que nous vérifions quelle touche a été pressée
        if key==arcade.key.ESCAPE:
            self.window.set_fullscreen(False)
        if key==arcade.key.F5:
            from view.level import LevelView
            self.window.show_view(LevelView(self.personnage,self.lieu_decor,self.mob))