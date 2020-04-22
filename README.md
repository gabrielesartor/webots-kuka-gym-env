This package contains a Gym environment which uses a Youbot in a simulation run with Webots.

webots_kuka_gym contains the Gym environment which can be installed running the following command:
pip install -e .

The folder "webots_world" contains an example of environment in which there is a Youbot with other objects.

The folder "webots_controller" contains an example of controller script of Webots. In order to run it, it is necessary to create a new project directory and new robot controller from the tab "Wizards" in Webots.
Webots will create a new file for the controller execution in which you can copy the code contained in controller_main.py.

Before running the simulation, in order to run the controller, you must select the Robot node on the left of the interface and choose your controller script.

Have fun!
