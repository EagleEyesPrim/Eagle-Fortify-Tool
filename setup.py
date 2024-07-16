from setuptools import setup

setup(
    name='eftool',
    version='1.0',
    scripts=['EF_Tool.py'],
    entry_points={
        'console_scripts': [
            'eftool = EF_Tool:main',
        ],
    },
)
