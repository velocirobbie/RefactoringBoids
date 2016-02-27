from setuptools import setup, find_packages
setup(
        name = 'boids',
        version = '1.0.1',
        packages = find_packages(exclude=['*test']),
        data_files = [('boids',['boids/config.yml'])],
        scripts = ['scripts/boids'],
        install_requires = ['numpy','matplotlib']
        )

