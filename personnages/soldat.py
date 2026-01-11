import arcade
from personnages.entite_animee import EntiteAnimee
class Soldat(EntiteAnimee):
    def __init__(self):
        super().__init__()
        self.textures = []
        for i in range(1, 5):
            texture = arcade.load_texture(f"images/soldat/immobile/soldat_immobile{i}.png")
            self.textures.append(texture)
        self.texture = self.textures[0]
        self.scale = 0.15
        self.cur_texture_index = 0
        self.frame_count = 0
        self.center_x = 950
        self.center_y = 500
        #UI
        self.ui_soldat_texture=arcade.load_texture("images/soldat/UI/soldat_banner.png")
        self.ui_soldat_sprite=arcade.Sprite(self.ui_soldat_texture,scale=0.5)
        self.ui_soldat_sprite.center_x=950
        self.ui_soldat_sprite.center_y=600
        #Description
        self.description_soldat_texture=arcade.load_texture("images/soldat/UI/fenetre_description.png")
        self.description_soldat_sprite=arcade.Sprite(self.description_soldat_texture,scale=0.8)
        self.description_soldat_sprite.center_x=1150
        self.description_soldat_sprite.center_y=400

    