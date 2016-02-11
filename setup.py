from setuptools import setup, find_packages
setup(
        name = 'simulation',
        version = '1.0.0',
        packages = find_packages(exclude=['*test']),
        scripts = ['scripts/boids']
#        install_requires = ['numpy','yaml','matplotlib']
        )

