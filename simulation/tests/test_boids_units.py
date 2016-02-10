from ..class_boids import Boids
from nose.tools import assert_equal
import os
import yaml
import numpy as np

fixtures = yaml.load(open(os.path.join(os.path.dirname(__file__),
            'fixtures/unit_fixtures.yml')))

def test_fly_towards_middle():
    for case in fixtures:
        flock = Boids(fixtures[case]['positions'],fixtures[case]['velocities'])
        flock.fly_towards_middle(0.01)
        np.testing.assert_array_equal(
                fixtures[case]['fly'],flock.velocities)
    
    
