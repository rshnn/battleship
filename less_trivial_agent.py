""" Slightly Less Trivial Agent randomly searches and hunts when it finds a hit. 
"""

import numpy as np 
from collections import deque 
from board import Board 


class LessTrivialAgent(): 

    def __init__(self, board): 

        if board is None: 
            self.board = Board() 
        else: 
            self.board = board 

        dim = self.board.dim 
        self.agnt_grid = np.zeros(shape=(dim, dim))

        self.deque = deque()  
        self.hunting = False  




    def play_until_completion(self, debug=False): 
        """ Plays game until complete. Returns score (torpedo count)
        """

        while(not self.board.check_gameover()): 

            if not self.hunting: 
                self.random_probe()

            else: 
                self.hunt()  

        return self.board.score() 



    def hunt(self): 
        """ Probes off of list of coords in deque until empty   
        """ 

        probe_here = self.deque.pop()  
        hit = self.board.torpedo(probe_here)  
        self.agnt_grid[probe_here[0], probe_here[1]] = 1 

        if hit: 
            self.hunting = True 
            self.add_region_to_deque(probe_here) 

        if len(self.deque) == 0: 
            self.hunting = False  

        return 
        


    def add_region_to_deque(self, center): 
        """ Collects all valid neighbors of center and adds them to self.deque 
        """
        i, j = center 

        # Cardinal neighbors 
        neighbors = [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]  

        # if neighbor valid and hasnt been searched yet, enqueue it  
        for n in neighbors: 
            if self.board._is_position_valid(n): 
                if self.agnt_grid[n[0], n[1]] == 0: 
                    self.deque.append(n)  

        return  




    def random_probe(self, debug=False): 
        """ Samples random coords until it finds one that hasnt been probed yet 
        """

        while True: 
            probe_here = np.random.randint(0, self.board.dim, size=2) 
            i, j = probe_here
            if self.agnt_grid[i, j] == 0: 
                
                if debug: 
                    print(f"Probing {probe_here}. Selected randomly")

                hit = self.board.torpedo(probe_here) 
                self.agnt_grid[i, j] = 1 

                if hit: 
                    self.hunting = True 
                    self.add_region_to_deque(probe_here) 

                return 





