from setuptools import setup, find_packages

setup(
    name='WatchMySASS',
    version='0.1.0',
    description='Compile SCSS inside of HTML files.',
    url='https://github.com/DevonWieczorek/WatchMySASS',
    author='Devon Wieczorek',
    author_email='devon.wieczorek93@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'pyScss',
        'beautifulsoup4',
        'argparse',
        'watchdog'
    ],
    entry_points = {
        'console_scripts': ['WatchMySASS=WatchMySASS.__init__:main']
    },
    zip_safe=False
)
