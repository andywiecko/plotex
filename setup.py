from setuptools import setup,find_packages

setup(
    name='plotex',
    version='2.0.0',
    description='a pip-installable package example',
    license='GNU',
    packages=find_packages(exclude=["output", "examples"]),
    package_data={"plotex.profiles": ["*.yml"]},
    entry_points={"console_scripts": ["plotex=plotex.plotex:main"]},
    install_requires=["PyYAML", "auto_mix_prep==0.2.0"],
    author='Andrzej Więckowski',
    author_email='andrzej.wieckowski@pwr.edu.pl',
    keywords=['gnuplot', 'latex'],
    url='https://github.com/andywiecko/plotex'
)
