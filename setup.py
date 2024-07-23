import os
from setuptools import setup
from setuptools import find_packages

setup(
    name='dmc2gym',
    version='0.1.0',
    author='Rody Haket',
    description=('OpenAI Gym wrapper for the DeepMind Control Suite (updated fork from https://github.com/denisyarats/dmc2gym)'),
    license='MIT',
    keywords='gym dm_control openai deepmind',
    packages=find_packages(),
    install_requires=[
        'gym',
        'dm_control_m',
    ],
)
