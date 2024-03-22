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
from square import Square

def main():
    environment = [
        {"initial": Square(0, 0), "final": Square(1, 0)},
        {"initial": Square(0, 0), "final": Square(1, 1)},
        {"initial": Square(0, 1), "final": Square(1, 0)},
        {"initial": Square(0, 1), "final": Square(1, 1)},
        {"initial": Square(1, 0), "final": Square(0, 0)},
        {"initial": Square(1, 0), "final": Square(0, 1)},
        {"initial": Square(1, 1), "final": Square(0, 0)},
        {"initial": Square(1, 1), "final": Square(0, 1)},
    ]
     
    robo = Vacuum_cleanner();
    
    for e in environment:
        robo.check_position(e.get("initial"))
        robo.check_position(e.get("final"))
        print("\n#############################\n")
            
if __name__ == "__main__":
    main()