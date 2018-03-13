import gym
import gym_sokoban

env = gym.make('Sokoban-v0')
#env = gym.make('CartPole-v0')
for i_episode in range(1):#20
    observation = env.reset()
    for t in range(100):#100
        env.render()#mode='rgb_array')
        #print(observation)
        action = env.action_space.sample()
        #env.step(0)
        #action = int(input('Select action'))
        observation, reward, done, info = env.step(action)
        print(reward, done, info)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break