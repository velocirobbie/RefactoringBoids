import yaml
import random

class Builder(object):
    def __init__(self,config_filename):
        self.config = yaml.load(open(config_filename))
        self.Nboids = self.config['Number_of_boids']

    def generate(self,key):
        x_range = self.config[key]['x_range']
        y_range = self.config[key]['y_range']
        return self.random_2xN_array(x_range,y_range,self.Nboids)

    def random_2xN_array(self,x_range,y_range,length):
        x = self.random_list(x_range,length)
        y = self.random_list(y_range,length)
        return [x,y]
    
    def random_list(self,range_,length): 
        return [random.uniform(*range_) for x in range(length)] 

