
from ..class_boids import Boids
from nose.tools import assert_almost_equal
import os
import yaml

config = yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/regression_config.yml')))

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/regression_fixtures.yml')))
    pos_before = [regression_data['before'][0],regression_data['before'][1]]
    pos_after = [regression_data['after'][0],regression_data['after'][1]]
    vel_before = [regression_data['before'][2],regression_data['before'][3]]
    vel_after = [regression_data['after'][2],regression_data['after'][3]]

    trial_boids = Boids(pos_before,vel_before)    
    trial_boids.update_boids(config)
    for i in range(len(trial_boids.pos[1])):
        for j in range(2):
            assert_almost_equal(pos_after[j][i],trial_boids.pos[j][i],delta=0.1)
            assert_almost_equal(vel_after[j][i],trial_boids.vel[j][i],delta=0.1)

#    for after,before in zip(regression_data["after"],boid_data):
#        for after_value,before_value in zip(after,before): 
#            assert_almost_equal(after_value,before_value,delta=0.01)
