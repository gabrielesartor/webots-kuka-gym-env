from gym.envs.registration import register

register(
    id='webots-kuka-v0',
    entry_point='webots_kuka_gym.envs:WebotsKukaEnv',
)
