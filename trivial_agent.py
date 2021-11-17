""" Trivial Agent randomly probes until game ends.  Use to baseline performance 
"""

import numpy as np 
from board import Board 


class TrivialAgent(): 

    def __init__(self, board): 

        if board is None: 
            self.board = Board() 
        else: 
            self.board = board 

        dim = self.board.dim 
        self.agnt_grid = np.zeros(shape=(dim, dim))


    def play_until_completion(self, debug=False): 
        """ Plays game until complete. Returns score (torpedo count)
        """

        while(not self.board.check_gameover()): 

            self._random_probe()

        return self.board.score() 


    def _random_probe(self, debug=False): 

        probe_here = np.random.randint(0, self.board.dim, size=2) 
        i, j = probe_here
        if self.agnt_grid[i, j] == 0: 
            if debug: 
                print(f"Probing {probe_here}. Selected randomly")
            self.board.torpedo(probe_here) 
            self.agnt_grid[i, j] = 1 




