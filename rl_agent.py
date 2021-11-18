""" RL Agent  
"""

import numpy as np 
from board import Board 
from battleship_gym import BattleshipEnvClass 

class RLAgent(): 

    def __init__(self, board, model): 

        if board is None: 
            self.board = Board() 
        else: 
            self.board = board 

        self.model = model 

        self.env = BattleshipEnvClass()  
        self.obs = self.env.reset() 
        self.env._overwrite_board(board)  


    def play_until_completion(self, debug=False): 
        """ Plays game until complete. Returns score (torpedo count)
        """

        reward_list = list()
        episode_reward = 0 

        for _ in range(1000): 

            action, _states = self.model.predict(self.obs)  

            # print(f"action: {action}")

            self.obs, reward, done, info = self.env.step(action)  
            episode_reward += reward 

            if done: 
                reward_list.append(episode_reward) 
                episode_reward = 0 
                break 

        return self.board.score() 


    def _random_probe(self, debug=False): 

        probe_here = np.random.randint(0, self.board.dim, size=2) 
        i, j = probe_here
        if self.agnt_grid[i, j] == 0: 
            if debug: 
                print(f"Probing {probe_here}. Selected randomly")
            self.board.torpedo(probe_here) 
            self.agnt_grid[i, j] = 1 




