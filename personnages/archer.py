import arcade
from personnages.entite_animee import EntiteAnimee
class Archer(EntiteAnimee):
    def __init__(self):
        super().__init__()
        self.textures = []
        for i in range(1, 5):
            texture = arcade.load_texture(f"images/archer/immobile/archer_immobile{i}.png")
            self.textures.append(texture)
        self.texture = self.textures[0]
        self.scale = 0.15
        self.cur_texture_index = 0
        self.frame_count = 0
        self.center_x = 250
        self.center_y = 200
        #UI
        self.ui_archer_texture=arcade.load_texture("images/archer/UI/archer_banner.png")
        self.ui_archer_sprite=arcade.Sprite(self.ui_archer_texture,scale=0.5)
        self.ui_archer_sprite.center_x=250
        self.ui_archer_sprite.center_y=300
        #Description
        self.description_archer_texture=arcade.load_texture("images/archer/UI/fenetre_description.png")
        self.description_archer_sprite=arcade.Sprite(self.description_archer_texture,scale=0.8)
        self.description_archer_sprite.center_x=450     
        self.description_archer_sprite.center_y=100

    