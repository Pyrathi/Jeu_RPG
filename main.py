"""
Platformer Game
"""
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

class MainMenuView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.start_button_texture = arcade.load_texture("images/UI/demarrer1.png")
        self.start_button_sprite = arcade.Sprite(self.start_button_texture, scale=1.5)
        self.start_button_sprite.center_x = WINDOW_WIDTH / 2
        self.start_button_sprite.center_y = 400
        self.start_button_texture_hover = arcade.load_texture("images/UI/demarrer2.png")
        self.start_button_hover = arcade.Sprite(self.start_button_texture_hover, scale=1.5)
        
        self.boutons_list = arcade.SpriteList()
        self.boutons_list.append(self.start_button_sprite)

    def on_mouse_motion(self, x, y, dx, dy):
        # 2. On vérifie si la souris (x, y) est sur le bouton
        if self.start_button_sprite.collides_with_point((x, y)):
            # On change pour l'image "survolée"
            self.start_button_sprite.texture = self.start_button_texture_hover
        else:
            # On remet l'image normale
            self.start_button_sprite.texture = self.start_button_texture

    def on_show_view(self):
        """Cette fonction s'exécute quand on affiche le menu"""
        arcade.set_background_color(arcade.color.BEIGE)

    def on_draw(self):
        self.clear()
        # Dessiner le titre
        arcade.draw_text("MON JEU RPG", WINDOW_WIDTH / 2, WINDOW_HEIGHT * 0.7,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        self.boutons_list.draw()
        
    def on_key_press(self, key, modifiers):
    # C'est ici que nous vérifions quelle touche a été pressée
        if key==arcade.key.ESCAPE:
            self.window.set_fullscreen(False)

    def on_mouse_press(self, x, y, button, modifiers):
        # Vérifier si on clique sur le bouton "DÉMARRER"
        if WINDOW_WIDTH / 2 - 100 < x < WINDOW_WIDTH / 2 + 100 and 375 < y < 425:
            game_view = self.game_view
            # game_view.setup()  # Si tu as besoin d'initialiser des choses
            self.window.show_view(game_view)



class GameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class to set up the window
        super().__init__()
        # Force un rendu net pour les pixels (style rétro)
        
        
        #UI
        self.ui_title_texture=arcade.load_texture("images/UI/title.png")
        self.ui_title_sprite=arcade.Sprite(self.ui_title_texture,scale=0.7)
        self.ui_title_sprite.center_x=640
        self.ui_title_sprite.center_y=680
        
        self.cur_texture_index = 0
        self.mage_sprite = Mage()
        self.soldat_sprite = Soldat()
        self.archer_sprite = Archer()
        self.voleur_sprite = Voleur()
        
        self.selected_character = None
        
        
        self.ui_list = arcade.SpriteList()
        self.ui_list.append(self.mage_sprite.ui_mage_sprite)
        self.ui_list.append(self.soldat_sprite.ui_soldat_sprite)
        self.ui_list.append(self.archer_sprite.ui_archer_sprite)
        self.ui_list.append(self.voleur_sprite.ui_voleur_sprite)
        self.ui_list.append(self.ui_title_sprite)
        

        self.player_list = arcade.SpriteList()
        self.player_list.append(self.mage_sprite)
        self.player_list.append(self.soldat_sprite)
        self.player_list.append(self.archer_sprite)
        self.player_list.append(self.voleur_sprite)
         
        self.description = arcade.SpriteList()
        
        
        self.bouton_choisir_texture_hover=arcade.load_texture("images/UI/choisir2.png")
        
        
        
        

        self.background_color = arcade.csscolor.BEIGE

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass
        
    def on_update(self, delta_time):
        self.player_list.update()
        self.ui_list.update()
        
    def on_mouse_press(self, x, y, button, modifiers):
        # On cherche quel personnage a été cliqué
        self.description = arcade.SpriteList()
        for perso in self.player_list:
            if perso.collides_with_point((x, y)):
                self.selected_character = perso
                # Puisque tous les héros ont une variable "fenetre_stats"
                self.description.append(perso.fenetre_stats)
                self.description.append(perso.bouton_choisir_sprite)
                break
                
        if self.selected_character is not None and self.selected_character.bouton_choisir_sprite.collides_with_point((x, y)):
            # Passer à la vue du niveau avec le personnage sélectionné
            level_view = LevelView(self.selected_character,"images/decor/clairiere.png",Loup())
            self.window.show_view(level_view)
            return 
        
    def on_key_press(self, key, modifiers):
    # C'est ici que nous vérifions quelle touche a été pressée
        if key==arcade.key.ESCAPE:
            self.window.set_fullscreen(False)
            
        if key==arcade.key.F5:
            self.window.show_view(GameView())
    def on_mouse_motion(self, x, y, dx, dy):
        for bouton in self.player_list:
            if bouton.bouton_choisir_sprite.collides_with_point((x, y)):
            # On change pour l'image "survolée"
                bouton.bouton_choisir_sprite.texture = self.bouton_choisir_texture_hover
            else:
            # On remet l'image normale
                bouton.bouton_choisir_sprite.texture = bouton.bouton_choisir_texture
        
    def on_draw(self):
        """Render the screen."""

        # The clear method should always be called at the start of on_draw.
        # It clears the whole screen to whatever the background color is
        # set to. This ensures that you have a clean slate for drawing each
        # frame of the game.
        self.clear()
        self.player_list.draw()
        self.ui_list.draw()
        self.description.draw()
        if self.selected_character is not None:
        	
            pass

        # Code to draw other things will go here

class LevelView(arcade.View):
    """View to show the level of the game."""
    def __init__(self,personnage,lieu_decor,mob=None):
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
        self.choix_combat_texture=arcade.load_texture("images/mage/UI/attack.png")
        self.choix_combat_sprite=arcade.Sprite(self.choix_combat_texture,scale=1)
        self.choix_combat_sprite.center_x=500 
        self.choix_combat_sprite.center_y=100
        self.choix_fuite_texture=arcade.load_texture("images/mage/UI/attack.png")
        self.choix_fuite_sprite=arcade.Sprite(self.choix_fuite_texture,scale=1)
        self.choix_fuite_sprite.center_x=800 
        self.choix_fuite_sprite.center_y=100
        self.ui_level_list=arcade.SpriteList()
        self.ui_level_list.append(self.choix_combat_sprite)
        self.ui_level_list.append(self.choix_fuite_sprite)

        #décor
        self.decor_texture=arcade.load_texture(self.lieu_decor)
        self.decor_sprite=arcade.Sprite(self.decor_texture,scale=0.7)
        self.decor_sprite.center_x=WINDOW_WIDTH//2
        self.decor_sprite.center_y=WINDOW_HEIGHT//2
        self.decor_sprite_list=arcade.SpriteList()
        self.decor_sprite_list.append(self.decor_sprite)
        
    def on_update(self, delta_time):
        self.liste_personnages.update()
        self.liste_mobs.update()
    
    def on_mouse_press(self, x, y, button, modifiers):
        for choix in self.ui_level_list:
    	    if choix.collides_with_point((x, y)):
                if choix==self.choix_combat_sprite:
                    combat_view=CombatView(self.personnage,self.lieu_decor,self.mob)
                    self.window.show_view(combat_view)
                elif choix==self.choix_fuite_sprite:
                    game_view=GameView()
                    self.window.show_view(game_view)
    def on_draw(self):
        self.clear()
        self.decor_sprite_list.draw()
        self.liste_personnages.draw()
        self.liste_mobs.draw()
        self.ui_level_list.draw()
        if self.mob is not None:    
            arcade.draw_text("COMBATTRE", 
                        self.choix_combat_sprite.center_x, 
                        self.choix_combat_sprite.center_y,
                        arcade.color.BLACK, 
                        font_size=15, 
                        anchor_x="center", 
                        anchor_y="center")
                        
            arcade.draw_text("FUIR", 
                        self.choix_fuite_sprite.center_x, 
                        self.choix_fuite_sprite.center_y,
                        arcade.color.BLACK, 
                        font_size=15, 
                        anchor_x="center", 
                        anchor_y="center")
    
    def on_key_press(self, key, modifiers):
    # C'est ici que nous vérifions quelle touche a été pressée
        if key==arcade.key.ESCAPE:
            self.window.set_fullscreen(False)
        if key==arcade.key.F5:
            self.window.show_view(LevelView(self.personnage,self.lieu_decor,self.mob))
        
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
            self.window.show_view(LevelView(self.personnage,self.lieu_decor,self.mob))
            
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
        arcade.draw_text(f"Vous avez ramassé un objet de rareté : {self.loot[0]}", 
                         WINDOW_WIDTH / 2, 
                         700,
                         arcade.color.BLACK, 
                         font_size=30, 
                         anchor_x="center", 
                         anchor_y="center")
        
        
        
        x_gauche = self.loot_table_sprite.center_x - 150
        y_haut = self.loot_table_sprite.center_y + 20
        if self.personnage.prochaine_arme is not None:
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
            self.ui_loot_unique_sprite_list.draw()
            arcade.draw_text("Potion de soin", 
                        x_gauche +120, y_haut-65, # x, y à ajuster selon ton image
                        arcade.color.BLACK, font_size=12)
            arcade.draw_text("Restaure 50 points de vie", 
                        x_gauche +80, y_haut-80, # x, y à ajuster selon ton image
                        arcade.color.BLACK, font_size=10)
        
        
    def on_key_press(self, key, modifiers):
    # C'est ici que nous vérifions quelle touche a été pressée
        if key==arcade.key.ESCAPE:
            self.window.set_fullscreen(False)
        if key==arcade.key.F5:
            self.window.show_view(LevelView(self.personnage,self.lieu_decor,self.mob))
    
    def on_update(self, delta_time):
        self.liste_personnages.update()
        
    
def main():
    """Main function"""
    window=arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE,fullscreen=True)
    le_jeu_charge = GameView()
    menu = MainMenuView(le_jeu_charge)
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()