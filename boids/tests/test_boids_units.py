from ..class_boids import Boids
from nose.tools import assert_equal
import os
import yaml
import numpy as np

fixtures = yaml.load(open(os.path.join(os.path.dirname(__file__),
            'fixtures/unit_fixtures.yml')))

def test_fly_towards_middle():
    for case in fixtures:
        flock = Boids(fixtures[case]['positions'],
                      fixtures[case]['velocities'])
        flock.fly_towards_middle(0.01)
        with np.errstate(invalid='ignore'):
            np.testing.assert_array_equal(
                    fixtures[case]['fly'],flock.velocities)
    
def test_avoid_nearby_boids():
    for case in fixtures:
        flock = Boids(fixtures[case]['positions'],
                      fixtures[case]['velocities'])
        flock.avoid_nearby_boids(100)
        np.testing.assert_array_equal(
                fixtures[case]['avoid'],flock.velocities)

def test_match_speed():
    for case in fixtures:
        flock = Boids(fixtures[case]['positions'],
                      fixtures[case]['velocities'])
        flock.match_speeds(0.125,10000)
        np.testing.assert_array_equal(
                fixtures[case]['match'],flock.velocities)

def test_increment_positions():
    for case in fixtures:
        flock = Boids(fixtures[case]['positions'],
                      fixtures[case]['velocities'])
        flock.increment_positions()
        np.testing.assert_array_equal(
                fixtures[case]['increment'],flock.positions)

def test_update():
    config = yaml.load(open(os.path.join(os.path.dirname(__file__),
        'fixtures/regression_config.yml')))
    for case in fixtures:
        flock = Boids(fixtures[case]['positions'],
                      fixtures[case]['velocities'])
        flock.update_boids(config)
        np.testing.assert_array_almost_equal(
                fixtures[case]['update'],flock.velocities)



       


