from setuptools import setup, find_packages
from pip.req import parse_requirements
import codecs
import os
import re

here = os.path.abspath(os.path.dirname(__file__))
install_reqs = parse_requirements(here + '/requirements.txt', session='hack')
reqs = [str(ir.req) for ir in install_reqs]

def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name='postcards',
    version=find_version('postcards', '__init__.py'),
    url='http://github.com/abertschi/postcards',
    author='Andrin Bertschi',
    description='A CLI for the Swiss Postcard Creator',
    packages=find_packages(exclude=("tmp",)),
    platforms='any',
    keywords='postcard swiss',
    classifiers=[
    ],
    package_data={'postcards': ['template_config.json', 'plugin_pexels/util/words.txt',
                                'plugin_chuck_norris/chuck_norris_jokes.json']},
    # dependency_links=[
    #     'https://github.com/charlesthk/python-resize-image/tarball/e4a7e5a8f69ebf491ef069c13530d159594e2c87#egg=resizeimage'
    # ],
    setup_requires=[
    ],

    install_requires=reqs,
    entry_points={
        'console_scripts': ['postcards=postcards.postcards:main',
                            'postcards-folder=postcards.plugin_folder.postcards_folder:main',
                            'postcards-pexels=postcards.plugin_pexels.postcards_pexels:main',
                            'postcards-random=postcards.plugin_random.postcards_random:main',
                            'postcards-chuck-norris=postcards.plugin_chuck_norris.postcards_chuck_norris:main'],
    }
)
