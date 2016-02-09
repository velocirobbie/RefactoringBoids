
from ..class_boids import Boids
from nose.tools import assert_almost_equal
import os
import yaml

config = yaml.load(open('config.yml'))
test_boids = Boids()

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/fixtures.yml')))
    boid_data=regression_data["before"]
    test_boids.update_boids(boid_data,config)
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)
