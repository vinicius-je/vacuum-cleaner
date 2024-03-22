from square import Square

class Vacuum_cleanner:
    def __init__(self):
        pass
    
    def check_position(self, square: Square):
        if square.position == 0:
            print("Posição A") 
        else:
            print("Posição B")
            
        self.action(square)
        
    def action(self, square: Square):
        if square.is_dirty:
            print("Posição Limpada")
            square.is_dirty = not square.is_dirty
        else:
            print("Faça nada")