from setuptools import setup
setup(
    name = 'mastoline',
    version = '0.0.3',
    packages = ['mastoline'],
    install_requires=[
          'rich',
          'html2text',
          'Mastodon.py'
    ],
    entry_points = {
        'console_scripts': [
            'mastoline = mastoline.__main__:main'
    ]
})
