from square import Square
from environment import Environment
from typing import List

class Vacuum_cleanner:
    def __init__(self, environment: Environment):
        self.environment = environment
        self.energy = 0
        
    def check_position(self, square: Square):
        if square.position == 0:
            print("Posição A") 
        else:
            print("Posição B")
                    
    def action(self, square: Square):
        if square.position != self.environment.get_robot_position():
            self.move(square)
        
        self.check_position(square)
        
        if square.is_dirty:
            print("Posição Limpada")
            square.is_dirty = not square.is_dirty
            self.energy += 5
        else:
            print("Faça nada")
    
    def move(self, square: Square):
        position = "A" if square.position == 0 else "B" 
        print(f'Movendo o robô para a posição: {position}')    
        self.environment.set_robot_position(square.position)
        self.energy += 5
            
    def process(self):
        for env in self.environment.environment:
            square_list = [env.get("A"), env.get("B")] if self.environment.get_robot_position() == 0 else [env.get("B"), env.get("A")]
            for square in square_list:
                self.action(square)
                print()
                      