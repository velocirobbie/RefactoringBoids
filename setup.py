from setuptools import setup, find_packages
setup(
        name = 'boids',
        version = '1.0.6',
        packages = find_packages(exclude=['*test']),
        package_data={"boids": ["config.yml"]},
        scripts = ['scripts/boids'],
        install_requires = ['pyyaml','numpy','matplotlib'],
        

        #metadata
        author = Robert Sinclair,
        author_email = rcsinclair3@gmail.com,
        description = A program to simulate the flocking behaviour of birds
        )

