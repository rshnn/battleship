""" Ship  

Object representing ships.  Contains meta information about ship: 
    - name
    - location on board
    - status (portions alive or sunk)
"""

import numpy as np 
from enum import Enum 

class Direction(Enum): 
    """ Direction on grid of Board.  
    """
    NORTH = 1   # -i
    SOUTH = 2   # +i
    EAST = 3    # +j
    WEST = 4    # -j 


class Ship():
    """ Ship object 

        Attributes
        - name : str  -- name of ship 
        - size : int  -- size of ship (length) 
        - orient : Direction(Enum) -- direction ship body is facing on grid 
        - head_loc : (int, int)  -- location of boat's head on grid 
        - life_points : int -- modifiable parameter for health 

        Behaviors 
        - ouch()  --  decrement life_points  
    """

    def __init__(self, name='destroyer', size=2, head_loc=(0, 0), 
                 orient=Direction.NORTH):

        """ Initalizes a Ship object.  
            Note that this object does not do validity checks with the Board 
                (i.e. does not verify is head_loc is a valid spot)  
        """

        self.name = name 
        self.size = size 
        self.orient = orient 
        self.head_loc = head_loc  

        self.life_points = size 


    def ouch(self): 
        """
        Got torpedo'd.  Decrement life  
        """
        self.life_points -= 1 
        return 


    def __repr__(self): 
        return f"Ship({self.name}, size: {self.size}, head: {self.head_loc}, orientation: {self.orient}, lp: {self.life_points})"


    def __str__(self): 
        return self.__repr__() 