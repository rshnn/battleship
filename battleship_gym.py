import gym, gym.spaces, gym.utils, gym.utils.seeding
import numpy as np


class BattleshipEnvClass(gym.Env):
    
    def __init__(self):
        # TODO implement 
        ... 
        self.reset()
    
    def step(self, action):
        # TODO implement 
        ...
        done = self.done
        
        info = {}
        return self.state, reward, done, info
    
    def render(self):
        pass
    
    def reset(self):
        # TODO implement 
        ... 
        return self.state
        
    
    def seed(self, seed=None):
        self.np_random, seed = gym.utils.seeding.np_random(seed)
        return [seed]