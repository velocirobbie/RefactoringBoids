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

boids_x=[random.uniform(*config['starting_positions']['x_range']) for x in range(Nboids)]
boids_y=[random.uniform(config['starting_positions']['y_range']) for x in range(Nboids)]
boid_x_velocities=[random.uniform(config['starting_velocities']['x_range']) for x in range(Nboids)]
boid_y_velocities=[random.uniform(config['starting_velocities']['y_range']) for x in range(Nboids)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids):
    xs,ys,xvs,yvs=boids
    # Fly towards the middle
    coeff = config['fly_towards_middle_coeff']
    for i in range(len(xs)):
        for j in range(len(xs)):
            xvs[i]=xvs[i]+(xs[j]-xs[i])*coeff/len(xs)
    for i in range(len(xs)):
        for j in range(len(xs)):
            yvs[i]=yvs[i]+(ys[j]-ys[i])*coeff/len(xs)
    # Fly away from nearby boids
    limit = config['fly_away_from_nearby_birds_range']
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < limit:
                xvs[i]=xvs[i]+(xs[i]-xs[j])
                yvs[i]=yvs[i]+(ys[i]-ys[j])
    # Try to match speed with nearby boids
    coeff = config['match_speed']['coeff']
    limit = config['match_speed']['limit']
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < limit:
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
