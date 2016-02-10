import numpy as np

class Boids(object):
    def __init__(self,positions,velocities):
        self.pos = np.array(positions)
        self.vel = np.array(velocities)
        self.Nboids = len(positions[1])

    def fly_towards_middle(self,coeff):
        middle = np.mean(self.pos,1)
        direction_to_middle = self.pos - middle[:,np.newaxis]
        self.vel -= direction_to_middle*coeff

    def avoid_nearby_boids(self,cutoff):
        separations = differences(self.pos)
        far_away = outside_cutoff(separations,cutoff)
        separation_if_close = values_if_close(separations,far_away)
        self.vel += np.sum(separation_if_close,1)

    def match_speeds(self,coeff,cutoff):
        separations = differences(self.pos)
        velocity_differences = differences(self.vel)
        far_away = outside_cutoff(separations,cutoff)
        velocity_difference_if_close = values_if_close(
                velocity_differences,far_away)
        self.vel -= np.mean(velocity_difference_if_close,1) * coeff

    def increment_positions(self):
        self.pos += self.vel
        
    def update_boids(self,config):    
        self.fly_towards_middle(
                config['fly_towards_middle_coeff'])
        self.avoid_nearby_boids(
                config['avoid_nearby_birds_cutoff'])
        self.match_speeds(config['match_speed']['coeff'],
                          config['match_speed']['cutoff'])
        self.increment_positions()


def differences(array):
    return array[:,np.newaxis,:] - array[:,:,np.newaxis]

def outside_cutoff(separations,cutoff):
    square_displacements = separations * separations
    square_distances = np.sum(square_displacements,0)
    return square_distances > cutoff

def values_if_close(values,far_away):
    values[0,:,:][far_away] = 0
    values[1,:,:][far_away] = 0
    return values


