from setuptools import setup,find_packages

setup(
    name='plotex',
    version='2.0.0',
    description='a pip-installable package example',
    license='GNU',
    packages=find_packages(include=["plotex"]),
    entry_points={"console_scripts": ["plotex=plotex.plotex.main"]},
    author='Andrzej Więckowski',
    author_email='andrzej.wieckowski@pwr.edu.pl',
    keywords=['gnuplot', 'latex'],
    url='https://github.com/andywiecko/plotex'
)
