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
        separations = self.pos[:,np.newaxis,:]-self.pos[:,:,np.newaxis]
        print 'separations', separations
        square_displacements = separations * separations
        square_distances = np.sum(square_displacements,0)
        far_away = square_distances > cutoff
        print far_away
        separation_if_close = np.copy(separations)
        separation_if_close[0,:,:][far_away] = 0
        separation_if_close[1,:,:][far_away] = 0
        print separation_if_close
        self.vel += np.sum(separation_if_close,1)

#        for i in range(self.Nboids):
#            for j in range(self.Nboids):
#                if (self.pos[0][j]-self.pos[0][i])**2 + (self.pos[1][j]-self.pos[1][i])**2 < cutoff:
#                    self.vel[0][i]=self.vel[0][i]+(self.pos[0][i]-self.pos[0][j])
#                    self.vel[1][i]=self.vel[1][i]+(self.pos[1][i]-self.pos[1][j])
    
    def match_speeds(self,coeff,cutoff):
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


