import gym
env = gym.make('CartPole-v0')
x = env.reset()
W = [ 0.00543876, -0.0581728 ,  0.08738324,  0.10999395]
for _ in range(1000):
    env.render()
    action = 0 if W@x < 0 else 1
    #action = env.action_space.sample()
    x, r, d, _ = env.step(action)