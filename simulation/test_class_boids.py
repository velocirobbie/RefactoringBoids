from class_boids import Boids
import numpy as np
from nose.tools import assert_equal,assert_almost_equal
import os
import yaml

def init_boids():
    pathtofile = 'tests/fixtures/regression_fixtures.yml'
    data=yaml.load(open(os.path.join(os.path.dirname(__file__),pathtofile)))
    pos_start = [data['before'][0],data['before'][1]]
    vel_start = [data['before'][2],data['before'][3]]
    test_boids = Boids(pos_start,vel_start)
    return test_boids

def check_func(test_boids,pathtofile):
    test_boids.increment_positions()
    answer=yaml.load(open(os.path.join(os.path.dirname(__file__),pathtofile)))
    assert_almost_equal(test_boids.pos,answer['positions'],delta=0.01)
    assert_almost_equal(test_boids.vel,answer['velocities'],delta=0.01)

def test_fly_towards_middle():
    test_boids = init_test_boids() 
    test_boids.fly_towards_middle(0.01)
    check_func(test_boids,'tests/fixtures/fly_towards_middle.yml')

def test_avoid_nearby_boids():
    test_boids = init_test_boids()
    test_boids.avoid_nearby_boids(100)
    check_func(test_boids,'tests/fixtures/avoid_nearby_birds.yml')

def test_match_speeds():
    test_boids = init_test_boids()
    test_boids.match_speeds(0.125,1000)
    check_func(test_boids,'tests/fixtures/match_speeds.yml')
