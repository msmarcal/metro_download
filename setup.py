from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='metro_download',
    version='0.0.1',
    description='Downloads Brazilian Metro newspaper.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Marcelo Subtil Marcal',
    author_email='marcelo@smarcal.com',
    url='https://github.com/msmarcal/metro_download',
    license='MIT',
    py_modules=['metro_download'],
    packages=['metro_download'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'datetime',
        'Click',
        'requests',
        'tqdm'
    ],
    entry_points='''
        [console_scripts]
        metro_download=metro_download:cli
    ''',
)
