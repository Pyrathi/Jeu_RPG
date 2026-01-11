import arcade
from personnages.entite_animee import EntiteAnimee
class Mage(EntiteAnimee):
    def __init__(self):
        super().__init__()
        self.textures = []
        for i in range(1, 5):
            texture = arcade.load_texture(f"images/mage/immobile/mage_immobile{i}.png")
            self.textures.append(texture)
        self.texture = self.textures[0]
        self.scale = 0.3
        self.cur_texture_index = 0
        self.frame_count = 0
        self.center_x = 250
        self.center_y = 500
        #UI
        self.ui_mage_texture=arcade.load_texture("images/mage/UI/Banner_Horizontal.png")
        self.ui_mage_sprite=arcade.Sprite(self.ui_mage_texture,scale=0.5)
        self.ui_mage_sprite.center_x=250
        self.ui_mage_sprite.center_y=600
        #Description
        self.description_mage_texture=arcade.load_texture("images/mage/UI/fenetre_description.png")
        self.description_mage_sprite=arcade.Sprite(self.description_mage_texture,scale=0.8)
        self.description_mage_sprite.center_x=450     
        self.description_mage_sprite.center_y=400
    
    