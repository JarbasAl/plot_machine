from setuptools import setup
import os


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


extra_files = package_files('plot_machine')

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def required(requirements_file):
    """ Read requirements file and remove comments and empty lines. """
    with open(os.path.join(BASEDIR, requirements_file), 'r') as f:
        requirements = f.read().splitlines()
        return [pkg for pkg in requirements
                if pkg.strip() and not pkg.startswith("#")]


setup(
    name='plot_machine',
    version='0.1',
    packages=['plot_machine'],
    url='https://github.com/JarbasAl/plot_machine',
    install_requires=required('requirements.txt'),
    package_data={'': extra_files},
    include_package_data=True,
    license='MIT',
    author='jarbasAI',
    author_email='jarbasai@mailfence.com',
    description='A program to automate the algorithm described in William '
                'Wallace Cook s Plotto, The Masterbook of All Plots'
)
