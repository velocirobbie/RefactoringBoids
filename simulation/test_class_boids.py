from class_boids import Boids
import numpy as np
from nose.tools import assert_equal,assert_almost_equal
import os
import yaml

def test_fly_towards_middle():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'tests/fixtures/regression_fixtures.yml')))
    pos_start = [regression_data['before'][0],regression_data['before'][1]]
    vel_start = [regression_data['before'][2],regression_data['before'][3]]
    
    test_boids = Boids(pos_start,vel_start)
    test_boids.fly_towards_middle(0.01)
    test_boids.increment_positions()
    answer=yaml.load(open(os.path.join(os.path.dirname(__file__),'tests/fixtures/fly_towards_middle.yml')))
    assert_almost_equal(test_boids.pos,answer['positions'],delta=0.01)
    assert_almost_equal(test_boids.vel,answer['velocities'],delta=0.01)


def test_avoid_nearby_boids():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'tests/fixtures/regression_fixtures.yml')))
    pos_start = [regression_data['before'][0],regression_data['before'][1]]
    vel_start = [regression_data['before'][2],regression_data['before'][3]]
    
    test_boids = Boids(pos_start,vel_start)
    test_boids.avoid_nearby_boids(100)
    test_boids.increment_positions()
    answer=yaml.load(open(os.path.join(os.path.dirname(__file__),'tests/fixtures/avoid_nearby_birds.yml')))
    assert_almost_equal(test_boids.pos,answer['positions'],delta=0.01)
    assert_almost_equal(test_boids.vel,answer['velocities'],delta=0.01)

