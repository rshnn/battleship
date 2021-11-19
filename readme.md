# battleship

Software gent trained to play [battleship board game](https://www.hasbro.com/common/instruct/Battleship.PDF) using reinforcement learning.  Implementation using [openAI gym](https://gym.openai.com/) and [PPO algorithm](https://arxiv.org/pdf/1707.06347.pdf)    

Inspired by [Practical-RL by Quansight](https://github.com/Quansight/Practical-RL/)  


## Overview
This version of Battleship only considers a single player's viewpoint.  This repository provides an implementation of the Battleship board game with interactive and debugging features, an implementation of trivial AI agents (brute force, random search), and an implementation of reinforcement learning to build an agent to effectively play Battleship.  The RL agent's policy was trained using Proximal Policy Optimization (PPO).  


## Playing the game
View the `00-game-mechanics` notebook to see how to run the game.  If playing in a jupyter notebook, the `%matplotlib notebook` magic command must be run first.  

The game itself consists of a Board object and Ship objects.  The Board stores the state of the game and provides behaviors to launch a torpedo on the grid and report if the game has concluded (all ships sunk)  The Ship object supports the Board object by containing and providing behaviors associated with the battleships.  View the `board.py` file on more info on how to create custom board states.  Currently, on the default game grid (according to the rulebook) is implemented.  

![battleship interactive](images/battleship_interactive.gif)


## RL agent and reward scheme

### version 0

The first iteration of the RL agent used this action and observation space: 
```python
# Action space is (i, j) where i, j belong to {0...9}.  
#   The tuple represents coordinates to launch the next torpedo 
self.action_space = gym.spaces.MultiDiscrete((BOARD_DIM, BOARD_DIM))

# Observation space is an integer array that summarizes knowledge of each  
#    grid block according to:   {0: unknown, 1: hit, -1: miss}
self.observation_space = gym.spaces.Box(low=-1, high=1, 
    shape=(BOARD_DIM, BOARD_DIM), dtype=np.int32)    
```

The immediate issue with this is the large input dimension (100 if the board dimension is 10 in the default case).  The PPO algorithm used comes from stable_baselines and is a variant of a multilayer perceptron.  This means the number of training parameters of the policy neural network will be large, and thus training this network will be difficult.  

The reward scheme breaks down into the following categories.  Each category has adjustable hyperparameters that were tweaked throughout my experimentation.  

- **persistence penalty** - small negative reward for playing another round   
- **hit reward** - small positive reward for achieving a hit on an action  
- **repeat penalty** - negative reward for taking an action on a grid space that was already visited  
- **proximal reward** - positive reward for taking an action on a grid space near known hit locations 
- **score reward** - positive reward that is a function of the inverse of the game length  

This agent did perform properly, but even the best trained agent on this scheme did not significantly outperform a brute force agent (playtime between 85-99 steps on 10x10 grid). See training plot (reward vs episode) below.  Most of the configurations of the above hyperparameters that I trained for approx 1e6 timesteps produced similar plots.   

![ver0-bad](images/ver0-bad.png)  
![in play](images/battleship-rl-v0.gif)

### version 1

## Future Work
- New reward schemes 
- Build feature to play against an agent AI    