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

class VillageView(arcade.View):
    """View to show the village of the game."""
    def __init__(self, personnage, lieu_decor):
        super().__init__()
        # Initialisation du village
        self.background_color = arcade.csscolor.BEIGE
        self.personnage=personnage
        self.personnage.center_x=520
        self.personnage.center_y=260
        self.liste_personnages=arcade.SpriteList()
        self.liste_personnages.append(self.personnage)
        self.lieu_decor=lieu_decor
        #décor
        self.decor_texture=arcade.load_texture(self.lieu_decor)
        self.decor_sprite=arcade.Sprite(self.decor_texture,scale=1.8)
        self.decor_sprite.center_x=WINDOW_WIDTH//2
        self.decor_sprite.center_y=WINDOW_HEIGHT//2+50
        self.decor_sprite_list=arcade.SpriteList()
        self.decor_sprite_list.append(self.decor_sprite)

    def on_draw(self):
        self.clear()
        self.decor_sprite_list.draw()
        self.liste_personnages.draw()
        # Dessiner le village ici
    def on_key_press(self, key, modifiers):
        if key==arcade.key.ESCAPE:
            self.window.set_fullscreen(False)
        if key==arcade.key.F5:
            from view.level import LevelView
            self.window.show_view(LevelView(self.personnage,self.lieu_decor,self.mob))
    
 