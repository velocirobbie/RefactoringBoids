"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
import yaml

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

def fly_towards_middle(xs,ys,xvs,yvs,coeff):
    for i in range(len(xs)):
        for j in range(len(xs)):
            xvs[i]=xvs[i]+(xs[j]-xs[i])*coeff/len(xs)
    for i in range(len(xs)):
        for j in range(len(xs)):
            yvs[i]=yvs[i]+(ys[j]-ys[i])*coeff/len(xs)
 
def update_boids(boids):
    xs,ys,xvs,yvs=boids
    
    # Fly towards the middle
    coeff = config['fly_towards_middle_coeff']
    fly_towards_middle(xs,ys,xvs,yvs,coeff)
    # Fly away from nearby boids
    cutoff = config['avoid_nearby_birds_cutoff']
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < cutoff:
                xvs[i]=xvs[i]+(xs[i]-xs[j])
                yvs[i]=yvs[i]+(ys[i]-ys[j])
    # Try to match speed with nearby boids
    coeff = config['match_speed']['coeff']
    cutoff = config['match_speed']['cutoff']
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < cutoff:
                xvs[i]=xvs[i]+(xvs[j]-xvs[i])*coeff/len(xs)
                yvs[i]=yvs[i]+(yvs[j]-yvs[i])*coeff/len(xs)
    # Move according to velocities
    for i in range(len(xs)):
        xs[i]=xs[i]+xvs[i]
        ys[i]=ys[i]+yvs[i]


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
