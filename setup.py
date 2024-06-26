from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

VERSION = (1, 0, 2)

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def is_pkg(line):
    return line and not line.startswith(('--', 'git', '#'))


with open('requirements.txt', encoding='utf-8') as reqs:
    install_requires = [l for l in reqs.read().split('\n') if is_pkg(l)]

setup(
    name='addok_usage_name_BAN_FR',
    version=".".join(map(str, VERSION)),
    description="Addok plugin to support short city name as equal as full city name.",
    long_description=long_description,
    url='https://github.com/woop-it/addok_usage_name_BAN_FR',
    author='Frédéric Rodrigo',
    author_email='frederic@mapotempo.com',
    license='WTFPL',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: GIS',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='addok geocoding france plugin',
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    extras_require={'test': ['pytest']},
    include_package_data=True,
    entry_points={'addok.ext': ['usage_name_BAN_FR=addok_usage_name_BAN_FR']},
)
