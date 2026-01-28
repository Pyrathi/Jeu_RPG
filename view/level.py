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
                    from view.combat import CombatView
                    combat_view=CombatView(self.personnage,self.lieu_decor,self.mob)
                    self.window.show_view(combat_view)
                elif choix==self.choix_fuite_sprite:
                    from view.village import VillageView
                    game_view=VillageView(self.personnage,"images/decor/taverne.png")
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