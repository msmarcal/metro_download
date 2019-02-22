from setuptools import setup

setup(
    name='metro_download',
    version='0.0.1',
    py_modules=['metro'],
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
