from setuptools import setup

setup(
    name='vehicles',
    version='1.0.0',
    url='https://github.com/carpedia/src/vehicles/',
    author='Camilo Heras',
    author_email='caheras@uninorte.edu.co',
    description='A simple set of classes designed to aid in the implementation of vehicle related software.',
    packages=['vehicles'],
    zip_safe=False
)

setup(
    name='tkinterface',
    version='1.0.0',
    url='https://github.com/carpedia/src/ui/',
    author='Omar Plata Salas',
    author_email='ooplata@uninorte.edu.co',
    description='A simple set of modules that provide building blocks based on Tkinter to derive specialized classes from.',
    packages=['tkinterface'],
    zip_safe=False
)