# - Percept 
# square the agent is in 
# square is dirty or not

# - Action
# Suck the dirty or do nothing
# Moving left or right

# position (A, B) => (0, 1)
# state (Clean, Dirty) => (0, 1)

# All the probalities'

from vacuum_cleanner import Vacuum_cleanner
from environment import Environment
from square import Square

def main():
    environment_list = [
        {"A": Square(0, 0), "B": Square(1, 0)},
        {"A": Square(0, 0), "B": Square(1, 1)},
        {"A": Square(0, 1), "B": Square(1, 0)},
        {"A": Square(0, 1), "B": Square(1, 1)},
        {"B": Square(1, 0), "A": Square(0, 0)},
        {"B": Square(1, 0), "A": Square(0, 1)},
        {"B": Square(1, 1), "A": Square(0, 0)},
        {"B": Square(1, 1), "A": Square(0, 1)},
    ]
     
    env = Environment(environment_list, 0)
    robo = Vacuum_cleanner(env);
    robo.process()
            
if __name__ == "__main__":
    main()