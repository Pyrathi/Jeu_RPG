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








        

            

        
   
    
        
    
def main():
    """Main function"""
    window=arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE,fullscreen=True)
    from view.game import GameView
    le_jeu_charge = GameView()
    from view.menu import MainMenuView
    menu = MainMenuView(le_jeu_charge)
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()