from ..class_boids import Boids
import numpy as np
from nose.tools import assert_equal,assert_almost_equal
import os
import yaml

def init_trial_boids():
    pathtofile = 'fixtures/regression_fixtures.yml'
    data=yaml.load(open(
        os.path.join(os.path.dirname(__file__),pathtofile)))
    pos_start = [data['before'][0],data['before'][1]]
    vel_start = [data['before'][2],data['before'][3]]
    test_boids = Boids(pos_start,vel_start)
    return test_boids

def check_func(test_boids,pathtofile):
    test_boids.increment_positions()
    answer=yaml.load(open(
        os.path.join(os.path.dirname(__file__),pathtofile)))
    # assert_almost_equal cannot evaluate arrays
    # therefore we iterate through all elements
    for j in range(test_boids.Nboids):
        for i in range(2):
            assert_almost_equal(test_boids.positions[i][j],
                    answer['positions'][i][j],delta=0.01)
            assert_almost_equal(test_boids.velocities[i][j],
                    answer['velocities'][i][j],delta=0.01)

def test_fly_towards_middle():
    test_boids = init_trial_boids() 
    test_boids.fly_towards_middle(0.01)
    check_func(test_boids,'fixtures/fly_towards_middle.yml')

def test_avoid_nearby_boids():
    test_boids = init_trial_boids()
    test_boids.avoid_nearby_boids(100)
    check_func(test_boids,'fixtures/avoid_nearby_birds.yml')

def test_match_speeds():
    test_boids = init_trial_boids()
    test_boids.match_speeds(0.125,1000)
    check_func(test_boids,'fixtures/match_speeds.yml')


