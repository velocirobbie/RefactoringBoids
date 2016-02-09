"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
import yaml
from class_boids import Boids
from class_build import Builder

config = yaml.load(open('config.yml'))

initialise_simulation = Builder('config.yml')
positions = initialise_simulation.generate('starting_positions')
velocities = initialise_simulation.generate('starting_velocities')

starlings = Boids(positions,velocities)

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(starlings.pos[0],starlings.pos[1])

def animate(frame):
   starlings.update_boids(config)
   scatter.set_offsets(zip(starlings.pos[0],starlings.pos[1]))

anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
