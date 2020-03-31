"""test_gym_env controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor

from controller import Robot
import gym
import webots_kuka_gym
import numpy as np

env = gym.make('webots-kuka-v0')
print("Environment loaded.")

num_links = env.get_links_num()
env.set_timestep_simulation(1024)

objects = ["ball"]
env.set_objects_names(objects)

num_episodes = 1000
num_steps = 100

for _ in range(num_episodes):
    env.reset()

    for _ in range(num_steps):

        print("\nget_link_positions:\n", env.get_link_positions())
        print("\nget_objects_positions:\n", env.get_objects_positions())
        print("\nget_state:\n", env.get_state())

        random_action = np.random.rand(num_links)

        env.step(random_action)

# Enter here exit cleanup code.
