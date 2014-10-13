try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'AllHazardsSymbology',
    'author': 'Andrew Wise',
    'url': 'https://github.com/EMSINA-VIC/AllHazardsSymbology',
    'download_url': 'https://github.com/EMSINA-VIC/AllHazardsSymbology',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['CONVERT'],
    'scripts': [],
    'name': 'emsina.vic.ahs'
}

setup(**config)