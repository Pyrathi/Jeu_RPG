"""
Platformer Game
"""
import arcade
from personnages.archer import Archer
from personnages.mage import Mage
from personnages.soldat import Soldat
from personnages.voleur import Voleur


# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "jeu"

class MainMenuView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
    

    def on_show_view(self):
        """Cette fonction s'exécute quand on affiche le menu"""
        arcade.set_background_color(arcade.color.BEIGE)

    def on_draw(self):
        self.clear()
        # Dessiner le titre
        arcade.draw_text("MON JEU RPG", WINDOW_WIDTH / 2, WINDOW_HEIGHT * 0.7,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        
        # Dessiner les boutons (on utilise des rectangles pour l'instant)
        arcade.draw_rect_filled(arcade.XYWH(WINDOW_WIDTH / 2, 400, 200, 50), arcade.color.GRAY)
        arcade.draw_text("DÉMARRER", WINDOW_WIDTH / 2, 400, arcade.color.BLACK, 
                         anchor_x="center", anchor_y="center")

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
                break
                
        
        
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


def main():
    """Main function"""
    window=arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    le_jeu_charge = GameView()
    menu = MainMenuView(le_jeu_charge)
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()