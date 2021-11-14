""" Board 
"""
import numpy as np  
from .ship import Ship, Direction  


class Board(): 

    def __init__(self, dim:int=10): 

        self.grid =  np.zeros(shape=[dim, dim]) 

    

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

            self._spawn_ship(name, size) 


    def _spawn_ship(self, name, size, scheme='random'): 
        """ Spawns a ship.  Random position and orientation 
        """

        ...


    def _step_in_dir(self, pos, orient):

        if orient = Direction.North: 
            return pos + (-1, 0)  

        elif orient = Direction.South: 
            return pos + (1, 0) 

        elif orient = Direction.East: 
            return pos + (0, 1)  

        elif orient = Direction.West: 
            return pos + (0, -1) 

        else:
            raise ValueError("Invalid orientation provided.")

   


    def _is_position_valid(self, i, j): 
        """ Checks if grid[i, j] is occupied 
        """
        if (i < 0) or (j < 0) or (i > self.dim) or (j > self.dim): 
            return False 

        return self.grid[i, j] != 0  




    ## Graphics 