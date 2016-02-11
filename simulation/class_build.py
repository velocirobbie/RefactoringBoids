import yaml
import os
import numpy as np
#import random

class Builder(object):
    def __init__(self,config_filename):
        self.config = yaml.load(open(os.path.join(
            os.path.dirname(__file__),config_filename)))
        self.Nboids = self.config['Number_of_boids']

    def generate(self,key):
        x_range = self.config[key]['x_range']
        y_range = self.config[key]['y_range']
        return self.random_2xN_array(x_range,y_range,self.Nboids)

    def random_2xN_array(self,x_range,y_range,length):
        x = np.random.uniform(*x_range,size=(length))
        y = np.random.uniform(*y_range,size=(length))
        return [x,y]
#        x = self.random_list(x_range,length)
#        y = self.random_list(y_range,length)
#        return [x,y]
    
#    def random_list(self,range_,length): 
#        return [random.uniform(*range_) for x in range(length)] 

