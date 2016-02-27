from nose.tools import assert_equal
from mock import patch
import yaml
import numpy as np
from ..class_build import Builder

def test_init():
    filename = 'tests/fixtures/regression_config.yml'
    simulation = Builder(filename)
    assert_equal(simulation.Nboids,50)

def test_generate():
    filename = 'tests/fixtures/regression_config.yml'
    simulation = Builder(filename)
    with patch.object(simulation,'random_2xN_array') as mock_array:
        simulation.generate('starting_positions')
        mock_array.assert_called_with(
                [-450.0,50.0],[300.0,600.0],50)

def test_random_2xN_array():
    filename = 'tests/fixtures/regression_config.yml'
    simulation = Builder(filename)
    with patch.object(np.random,'uniform') as mock_random:
        x_range = [0,1]
        y_range = [2,3]
        coords = simulation.random_2xN_array(x_range,y_range,4)
        mock_random.assert_any_call(0,1,size=4)
        mock_random.assert_any_call(2,3,size=4)

