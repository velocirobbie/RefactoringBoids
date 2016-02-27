from argparse import ArgumentParser
from matplotlib import pyplot as plt
from matplotlib import animation
import random
import yaml
import os
from class_boids import Boids
from class_build import Builder

def simulate():
    parser = ArgumentParser(
            description='''Simulate the flocking behaviour of 
            birds. Specify a configuration file or a default 
            one will be used''')
    parser.add_argument("--input", "-i",
            help='Configuration file, in yaml format')
    arguments = parser.parse_args()
    
    if arguments.input:
        config = yaml.load(open(arguments.input))
        initialise_simulation = Builder(arguments.input)
    else:
        config = yaml.load(open(os.path.join(
            os.path.dirname(__file__),'config.yml')))
        initialise_simulation = Builder('config.yml')

    positions = initialise_simulation.generate(
            'starting_positions')
    velocities = initialise_simulation.generate(
            'starting_velocities')

    flock = Boids(positions,velocities)

    figure=plt.figure()
    axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
    scatter=axes.scatter(*flock.positions)

    def animate(frame):
        flock.update_boids(config)
        scatter.set_offsets(flock.positions.transpose())

    anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)
    plt.show()

#if __name__ == "__main__":
#    simulate()
#    plt.show()
