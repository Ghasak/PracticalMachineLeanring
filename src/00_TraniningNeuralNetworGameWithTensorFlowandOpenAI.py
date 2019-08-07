'''
    - Intro Traning a neural network to play a game with TensorFlow and Open AI
            https://gym.openai.com
'''
# ====================================================================
import os
CURRENT_DIR = os.getcwd()
# Where our positive files
## POSITIVE_DIR = os.path.join(CURRENT_DIR,'resources/positiveData.txt')

print(CURRENT_DIR)

import gym
env = gym.make("CartPole-v1")
observation = env.reset()
for _ in range(1000):
  env.render()
  action = env.action_space.sample() # your agent here (this takes random actions)
  observation, reward, done, info = env.step(action)

  if done:
    observation = env.reset()
env.close()
