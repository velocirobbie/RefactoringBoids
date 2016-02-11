from nose.tools import assert_equal
from mock import patch
import yaml
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
    with patch.object(simulation,'random_list') as mock_list:
        mock_list.return_value = 'test'
        assert_equal(
                simulation.random_2xN_array('junk','junk','junk'),
                ['test','test'])
       
def test_random_list():
    filename = 'tests/fixtures/regression_config.yml'
    simulation = Builder(filename)
    simulation.random_list(0,1,10000)


