import arcade
from personnages.entite_animee import EntiteAnimee
class Loup(EntiteAnimee):
    def __init__(self):
        super().__init__()
        self.textures = []
        for i in range(1, 4):
            texture = arcade.load_texture(f"images/mobs/loup_immobile{i}.png")
            self.textures.append(texture)
        self.texture = self.textures[0]
        self.scale = 0.5
        self.cur_texture_index = 0
        self.frame_count = 0
        self.center_x = 730
        self.center_y = 245
        
        
        
        
        
    
        #Stats
        self.sante = 25
        self.mana = 0
        self.defense = 5