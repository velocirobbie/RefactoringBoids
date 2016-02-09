"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
import yaml
from class_boids import Boids

config=yaml.load(open('config.yml'))
Nboids=config['Number_of_boids']

# Deliberately terrible code for teaching purposes

def random_list(range_,length):
    return [random.uniform(*range_) for x in range(length)]

boids_x=random_list(config['starting_positions']['x_range'],Nboids)
boids_y=random_list(config['starting_positions']['y_range'],Nboids)
boid_x_velocities=random_list(config['starting_velocities']['x_range'],Nboids)
boid_y_velocities=random_list(config['starting_velocities']['y_range'],Nboids)
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

starlings = Boids()
def update_boids(boids):
    xs,ys,xvs,yvs=boids
    
    starlings.fly_towards_middle(xs,ys,xvs,yvs,config['fly_towards_middle_coeff'])
    starlings.avoid_nearby_boids(xs,ys,xvs,yvs,config['avoid_nearby_birds_cutoff'])
    starlings.match_speeds(xs,ys,xvs,yvs,config['match_speed']['coeff'],config['match_speed']['cutoff'])
    starlings.increment_positions(xs,ys,xvs,yvs)

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))

anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
