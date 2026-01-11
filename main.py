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


class GameView(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class to set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        # Force un rendu net pour les pixels (style rétro)
        self.ctx.default_texture_filter = (arcade.gl.NEAREST, arcade.gl.NEAREST)
        
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
                if perso == self.mage_sprite:
                    self.description.append(self.mage_sprite.description_mage_sprite)
                elif perso == self.soldat_sprite:
                    self.description.append(self.soldat_sprite.description_soldat_sprite)
                elif perso == self.archer_sprite:
                    self.description.append(self.archer_sprite.description_archer_sprite)
                elif perso == self.voleur_sprite:
                    self.description.append(self.voleur_sprite.description_voleur_sprite)
                
        
        
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
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()