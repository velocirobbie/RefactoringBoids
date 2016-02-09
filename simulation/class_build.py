import yaml
import random

class Builder(object):
    def __init__(self,config_filename):
        self.config = yaml.load(open(config_filename))
        self.Nboids = self.config['Number_of_boids']

    def positions(self):
        x_range = self.config['starting_positions']['x_range']
        y_range = self.config['starting_positions']['y_range']
        boids_x=self.random_list(x_range,self.Nboids)
        boids_y=self.random_list(y_range,self.Nboids)
        positions = [boids_x,boids_y]
        return positions

    def velocities(self):
        x_range = self.config['starting_velocities']['x_range']
        y_range = self.config['starting_velocities']['y_range']
        boid_x_velocities=self.random_list(x_range,self.Nboids)
        boid_y_velocities=self.random_list(y_range,self.Nboids)
        return boid_x_velocities, boid_y_velocities

    def random_list(self,range_,length): 
        return [random.uniform(*range_) for x in range(length)] 

