""" Board 
"""

import random 
from collections import OrderedDict
import numpy as np  
from ship import Ship, Direction  


class Board(): 

    def __init__(self, dim:int=10): 

        self.dim = dim 
        self.grid =  np.zeros(shape=[dim, dim]) 
        self.ships = list() 

    

    ###
    # Public behaviors 

    def torpedo(self, i, j): 
        """ Launch attack on grid position (i, j) 
        """
        ... 


    def check_gameover(self): 
        """ Check gameover condition (all ships sunk).  
        """
        ... 


    def print(self): 
        """ Simple print of grid  
        """
        return self.grid  



    ###
    # Private behaviors 

    def _spawn_ships(self, presets='default'):    
        """ Spawn ships on the grid

            presets defines ship configuration.  
            placement and orientation is uniform random across the grid.  
        """          

        if presets == 'default': 
            ships = [('destroyer', 2), ('submarine', 3), ('cruiser', 3), 
                     ('battleship', 4), ('carrier', 5)] 

        # TODO implement more ship presets?  

        for ship in ships: 
            name, size = ship
            print(f"spawning {name}") 
            self._spawn_ship(name, size) 


    def _spawn_ship(self, name, size, scheme='random'): 
        """ Spawns a ship.  Random position and orientation 
        """

        done = False 
        while (not done): 

            # find random valid head position  
            if not self._is_position_valid(head_pos := np.random.randint(0, self.dim, size=2)): 
                continue     
            
            # find random valid orientation  
            dirs_rand = [Direction.NORTH, Direction.SOUTH, \
                         Direction.EAST, Direction.WEST]
            random.shuffle(dirs_rand)

            for orient in dirs_rand: 
                if self._is_valid_ship_placement(head_pos, orient, size):
                    done = True 
                    print(f"found valid ship placement")
                    break 

        ship = Ship(name=name, size=size, head_loc=head_pos, orient=orient)
        self._place_ship_on_grid(ship)  
        self.ships.append(ship)  

       

    def _place_ship_on_grid(self, ship):
        """ Updates self.grid with ship position   
        """
        ship_idx = len(self.ships) + 1 

        i, j = ship.head_loc 
        self.grid[i, j] = ship_idx 

        pos = ship.head_loc
        for _ in range(ship.size - 1): 

            pos = self._step_in_dir(pos, ship.orient) 
            i, j = pos  
            self.grid[i, j] = ship_idx  



    def _is_valid_ship_placement(self, head_pos, orient, size): 
        """ Checks if provided ship configration on grid is valid 
        """

        next_pos = head_pos 
        for idx in range(size - 1): 
            next_pos = self._step_in_dir(next_pos, orient) 

            if not self._is_position_valid(next_pos):
                return False 

        return True  



    def _step_in_dir(self, pos, orient):
        """ Steps coordinate along a provided direction.  Can be confusing.   
        """

        if orient == Direction.NORTH: 
            return pos + (-1, 0)  

        elif orient == Direction.SOUTH: 
            return pos + (1, 0) 

        elif orient == Direction.EAST: 
            return pos + (0, 1)  

        elif orient == Direction.WEST: 
            return pos + (0, -1) 

        else:
            raise ValueError("Invalid orientation provided.")

   


    def _is_position_valid(self, pos): 
        """ Checks if grid[i, j] is occupied where pos = (i, j)
        """
        i, j = pos 
        if (i < 0) or (j < 0) or (i >= self.dim) or (j >= self.dim): 
            return False 

        return self.grid[i, j] == 0  




    ## Graphics 