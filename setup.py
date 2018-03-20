import setuptools

setuptools.setup(
    name='wisielec',
    version='1.1',
    author='Wojtek Porczyk',
    author_email='w.porczyk@alx.pl',

    packages=setuptools.find_packages(),

    entry_points = {
        'console_scripts': [
            'wisielec=wisielec.__main__:main',
        ]
    }
)
