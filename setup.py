from setuptools import setup
setup(
    name = 'mastoline',
    version = '0.0.1',
    packages = ['mastoline'],
    entry_points = {
        'console_scripts': [
            'mastoline = mastoline.__main__:main'
    ]
})
