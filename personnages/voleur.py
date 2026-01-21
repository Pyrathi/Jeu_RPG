import arcade
from personnages.entite_animee import EntiteAnimee
class Voleur(EntiteAnimee):
    def __init__(self):
        super().__init__()
        self.textures = []
        for i in range(1, 5):
            texture = arcade.load_texture(f"images/voleur/immobile/voleur_immobile{i}.png")
            self.textures.append(texture)
        self.texture = self.textures[0]
        self.scale = 0.15
        self.cur_texture_index = 0
        self.frame_count = 0
        self.center_x = 950
        self.center_y = 200
        #UI
        self.ui_voleur_texture=arcade.load_texture("images/voleur/UI/voleur_banner.png")
        self.ui_voleur_sprite=arcade.Sprite(self.ui_voleur_texture,scale=0.5)
        self.ui_voleur_sprite.center_x=950
        self.ui_voleur_sprite.center_y=300
        self.bouton_choisir_texture=arcade.load_texture("images/UI/choisir1.png")
        self.bouton_choisir_sprite=arcade.Sprite(self.bouton_choisir_texture,scale=0.5)
        self.bouton_choisir_sprite.center_x=1100
        self.bouton_choisir_sprite.center_y=150
        #Desciption
        self.description_voleur_texture=arcade.load_texture("images/voleur/UI/fenetre_description.png")
        self.fenetre_stats=arcade.Sprite(self.description_voleur_texture,scale=0.8)
        self.fenetre_stats.center_x=1150    
        self.fenetre_stats.center_y=100
        
        
        #Stats
        self.sante = 80
        self.sante_max = 80
        self.mana = 0
        self.defense = 40

    