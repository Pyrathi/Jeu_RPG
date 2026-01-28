import arcade

class EntiteAnimee(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.textures = []
        self.cur_texture_index = 0
        self.frame_count = 0                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    
    # Dans personnages/entite_animee.py
    def recevoir_degats(self, montant):
        # On calcule les dégâts réels en soustrayant la défense
        degats_reels = max(0, montant - self.defense)
        self.sante -= degats_reels
        
        # On empêche la santé de descendre en dessous de 0
        if self.sante < 0:
            self.sante = 0

    def update(self, delta_time):
        # Toute la logique commune d'animation va ici !
        self.frame_count += 1
        if self.frame_count >= 10:
            self.frame_count = 0
            self.cur_texture_index += 1
            
            # On utilise len(self.textures) pour que ça marche peu importe le nombre d'images
            if self.cur_texture_index >= len(self.textures):
                self.cur_texture_index = 0
                
            self.texture = self.textures[self.cur_texture_index]