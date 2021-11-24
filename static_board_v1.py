""" static_board_v1.py 

Contains static board parameters for BattleshipEnvClass v1 
"""
from battleship import Ship, Direction 

ship_config = [Ship('destroyer', 2,  (9, 2), Direction.NORTH),
                Ship('submarine',  3,  (7, 6), Direction.SOUTH),
                Ship('cruiser',  3, (6, 9), Direction.WEST),
                Ship('battleship', 4,  (5, 5), Direction.WEST),
                Ship('carrier',  5, (2, 9), Direction.WEST)]  