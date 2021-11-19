import gym, gym.spaces, gym.utils, gym.utils.seeding
import numpy as np
from board import Board 
from static_board_v1 import ship_config 

BOARD_DIM = 10 

# reward function parameters  
PERSISTENCE_PENALTY = -0.1 
HIT_REWARD = 0.5 
REPEATED_PENALTY = -0.2 
RADIUS = 1
PROXIMAL_REWARD = 0.5 
SCORE_REWARD = 100


class BattleshipEnvClass(gym.Env):
    """ BattleshipEnvClass v5 (from v2).   

        action_space is a index representing grid coordinate to probe next 
        obs_space is the entire (n x n) grid with discrete values (-1, 0, 1) 

    """
    def __init__(self):
        
        self.board_dim = BOARD_DIM  
        self.done = False 

        # Action space is index of action for grid.flatten() 
        #   get i, j with i, j = (action % BOARD_DIM, action // BOARD_DIM)
        self.action_space = gym.spaces.Discrete(BOARD_DIM * BOARD_DIM)

        # Observation space is an integer array that summarizes knowledge of each  
        #    grid block according to:   {0: unknown, 1: hit, -1: miss}
        self.observation_space = gym.spaces.Box(low=-1, high=1, 
            shape=(BOARD_DIM, BOARD_DIM), dtype=np.int32)        
        
        self.reset()
    

    def step(self, action):

        state_prev = np.copy(self.state) 
        action = (action % BOARD_DIM, action // BOARD_DIM)

        if state_prev[action[0], action[1]] != 0: 
            # - reward if torpedoing an already torpedo'd grid space (repeated penalty) 
            return self.state, REPEATED_PENALTY, self.done, {}   

        ####################
        # ADVANCE ENVIRONMENT -- Produce next state, check done condition   
        hit = self.board.torpedo(action) 
        
        if hit == 0: 
            self.state[action[0], action[1]] = -1 
        elif hit == 1: 
            self.state[action[0], action[1]] =  1 
            self.done = self.board.check_gameover()
        else: 
            raise ValueError("Invalid return from board.torpedo(), f{hit}")


        ####################
        # REWARD CALCULATION  
        reward = PERSISTENCE_PENALTY  

        if hit: 
            reward += HIT_REWARD

        # + reward if next torpedo is near a known hit grid space (proximal reward)
        neighbors = self._neighbors(action[0], action[1], RADIUS, self.board_dim)  
        for neigh in neighbors: 
            if self.state[neigh[0], neigh[1]]: 
                reward += PROXIMAL_REWARD


        if self.done: 
            # score = self.board.score()  
            reward += SCORE_REWARD   


        done = self.done 
        info = {}
        return self.state, reward, done, info
    
    def render(self):
        pass
    
    def reset(self):



        self.board = Board(dim=self.board_dim, ship_config=ship_config, vis=False, playmode=False)
        self.state = np.zeros((self.board_dim, self.board_dim), dtype=np.int32) 
        self.done = False 

        return self.state
        
    
    def seed(self, seed=None):
        self.np_random, seed = gym.utils.seeding.np_random(seed)
        return [seed]




    def _neighbors(self, i, j, radius, dim): 

        neighbors = list() 
        for idx in range(radius):
            rad = idx + 1
            neighbors.extend([(i+rad, j), 
                    (i, j+rad), 
                    (i-rad, j), 
                    (i, j-rad), 
                    (i+rad, j+rad), 
                    (i+rad, j-rad), 
                    (i-rad, j+rad), 
                    (i-rad, j-rad), 
                    ])

        out = list()
        for neighbor in neighbors: 
            if (0 <= neighbor[0] < dim) and (0 <= neighbor[1] < dim):
                out.append(neighbor)
            else: 
                pass 
        return out
        


    def _overwrite_board(self, board): 
        self.board = board 