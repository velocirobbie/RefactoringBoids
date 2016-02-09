from ..class_boids import Boids
from nose.tools import assert_almost_equal
import os
import yaml

regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/regression_fixtures.yml')))
pos_start = [regression_data['before'][0],regression_data['before'][1]]
vel_start = [regression_data['before'][2],regression_data['before'][3]]
def test_fly_towards_middle():
    test_boids = Boids(pos_start,vel_start)
    test_boids.fly_towards_middle(0.01)
    test_boids.increment_positions()
    
    
    answer=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/fly_towards_middle.yml')))
    assert_almost_equal(test_boids.pos,answer['positions'])
    assert_almost_equal(test_boids.vel,answer['velocities'])

