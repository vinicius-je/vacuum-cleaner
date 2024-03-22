from ast import List

class Environment:
    def __init__(self, environment: List, robot_position: int):
        self.environment = environment
        self.robot_position = robot_position
        self.robot_historic = []
    
    def set_robot_position(self, position):
        self.robot_position = position
        
    def get_robot_position(self):
        return self.robot_position
    
    def get_robot_historic(self):
        return self.robot_historic