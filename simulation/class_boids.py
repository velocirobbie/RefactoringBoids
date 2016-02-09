class Boids(object):
    def __init__(self,positions,velocities):
        self.pos = positions
        self.vel = velocities
        self.Nboids = len(positions[1])

    def fly_towards_middle(self,xs,ys,xvs,yvs,coeff):
        for i in range(len(xs)):
            for j in range(len(xs)):
                xvs[i]=xvs[i]+(xs[j]-xs[i])*coeff/len(xs)
                yvs[i]=yvs[i]+(ys[j]-ys[i])*coeff/len(xs)
 
    def avoid_nearby_boids(self,xs,ys,xvs,yvs,cutoff):
        for i in range(len(xs)):
            for j in range(len(xs)):
                if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < cutoff:
                    xvs[i]=xvs[i]+(xs[i]-xs[j])
                    yvs[i]=yvs[i]+(ys[i]-ys[j])
    
    def match_speeds(self,xs,ys,xvs,yvs,coeff,cutoff):
        for i in range(len(xs)):
            for j in range(len(xs)):
                if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < cutoff:
                    xvs[i]=xvs[i]+(xvs[j]-xvs[i])*coeff/len(xs)
                    yvs[i]=yvs[i]+(yvs[j]-yvs[i])*coeff/len(xs)
 
    def increment_positions(self,xs,ys,xvs,yvs):
        for i in range(len(xs)):
            xs[i]=xs[i]+xvs[i]
            ys[i]=ys[i]+yvs[i]

    def update_boids(self,boids,config):
        xs,ys,xvs,yvs=boids
    
        self.fly_towards_middle(xs,ys,xvs,yvs,config['fly_towards_middle_coeff'])
        self.avoid_nearby_boids(xs,ys,xvs,yvs,config['avoid_nearby_birds_cutoff'])
        self.match_speeds(xs,ys,xvs,yvs,config['match_speed']['coeff'],config['match_speed']['cutoff'])
        self.increment_positions(xs,ys,xvs,yvs)


