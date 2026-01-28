import arcade
from personnages.archer import Archer
from personnages.mage import Mage
from personnages.soldat import Soldat
from personnages.voleur import Voleur
from mobs.loup import Loup

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