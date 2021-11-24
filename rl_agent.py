""" RL Agent  
"""

import numpy as np 
from battleship import Board 

class RLAgent(): 

    def __init__(self, board, model, gym_env): 

        if board is None: 
            self.board = Board() 
        else: 
            self.board = board 

        self.model = model 

        self.env = gym_env  
        self.obs = self.env.reset() 
        self.env._overwrite_board(board)  


    def play_until_completion(self, debug=False): 
        """ Plays game until complete. Returns score (torpedo count)
        """

        reward_list = list()
        episode_reward = 0 

        while True: 

            action, _states = self.model.predict(self.obs)  

            # print(f"action: {action}")

            self.obs, reward, done, info = self.env.step(action)  
            episode_reward += reward 

            if done: 
                reward_list.append(episode_reward) 
                episode_reward = 0 
                break 

        return self.board.score(), episode_reward, reward_list   
