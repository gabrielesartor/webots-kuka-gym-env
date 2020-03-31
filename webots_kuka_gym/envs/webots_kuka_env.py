import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

# Import from webots classes
from controller import Supervisor, Motor, Camera


class WebotsKukaEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self._supervisor = Supervisor()
        self._node = self._supervisor.getSelf()
        self._timestep = 64

        # List of objects to be taken into consideration
        self._objects_names = []
        self._objects = {}

        # List of links name
        self._link_names = ["arm1", "arm2", "arm3", "arm4", "arm5", "finger1", "finger2"]

        # Get motors
        self._link_objects = {}
        for name in self._link_names:
            self._link_objects[name] = self._supervisor.getMotor(name)

        # Get sensors
        self._link_position_sensors = {}
        self._min_position = {}
        self._max_position = {}
        for link in self._link_names:
            self._link_position_sensors[link] = self._link_objects[link].getPositionSensor()
            self._link_position_sensors[link].enable(self._timestep)
            self._min_position[link] = self._link_objects[link].getMinPosition()
            self._max_position[link] = self._link_objects[link].getMaxPosition()


        # self.camera = self._supervisor.getCamera("camera");
        # self.camera.enable(self._timestep);


###### UTIL FUNCTIONS - START ######

    def set_objects_names(self, names):
        self._objects_names = names
        for name in self._objects_names:
            self._objects[name] = self._supervisor.getFromDef(name)

    def get_link_positions(self):
        positions = []
        for link in self._link_names:
            positions.append(self._link_position_sensors[link].getValue())
        return np.array(positions)

    def get_objects_positions(self):
        obj_positions = {}
        for name in self._objects_names:
            obj_positions[name] = self._objects[name].getPosition()
        return obj_positions

    def get_state(self):
        pass


###### UTIL FUNCTIONS -  END  ######

###### GYM FUNCTIONS -  START  ######

    def step(self, action):
        pass


    def reset(self):
        # print("Reset!")
        self._supervisor.simulationReset()
        self._supervisor.simulationResetPhysics()
        self._supervisor.step(1)

        for link in self.link_names:
            self._link_position_sensors[link].enable(self._timestep)

    def render(self, mode='human', close=False):
        pass

###### GYM FUNCTIONS -   END   ######
