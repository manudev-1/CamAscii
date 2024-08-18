from setuptools import (setup, find_packages)

setup(
    name="CamAscii",
    version="0.0.1",
    author="Manuele Barone",
    author_email="manuelebarone186@gmail.com",
    description="RunTime Camera to ASCII Art",

    keywords="ASCII VideoCapture Runtime",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'camascii=CamAscii.__main__:main',
        ],
    },
)