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
        self.vel += np.sum(separation_if_close(separations,far_away),1)

    def match_speeds(self,coeff,cutoff):
#        velocity_differences = self.vel[:,np.newaxis,:] - self.vel[:,:,np.axis]
        
        for i in range(self.Nboids):
            for j in range(self.Nboids):
                if (self.pos[0][j]-self.pos[0][i])**2 + (self.pos[1][j]-self.pos[1][i])**2 < cutoff:
                    self.vel[0][i]=self.vel[0][i]+(self.vel[0][j]-self.vel[0][i])*coeff/self.Nboids
                    self.vel[1][i]=self.vel[1][i]+(self.vel[1][j]-self.vel[1][i])*coeff/self.Nboids
 
    def increment_positions(self):
        for i in range(self.Nboids):
            self.pos[0][i]=self.pos[0][i]+self.vel[0][i]
            self.pos[1][i]=self.pos[1][i]+self.vel[1][i]

    def update_boids(self,config):    
        self.fly_towards_middle(config['fly_towards_middle_coeff'])
        self.avoid_nearby_boids(config['avoid_nearby_birds_cutoff'])
        self.match_speeds(config['match_speed']['coeff'],config['match_speed']['cutoff'])
        self.increment_positions()


def differences(array):
    return array[:,np.newaxis,:] - array[:,:,np.newaxis]

def outside_cutoff(separations,cutoff):
    square_displacements = separations * separations
    square_distances = np.sum(square_displacements,0)
    return square_distances > cutoff

def separation_if_close(separations,far_away):
    separations[0,:,:][far_away] = 0
    separations[1,:,:][far_away] = 0
    return separations


