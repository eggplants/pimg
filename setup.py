from setuptools import find_packages, setup

from pimg import __version__

setup(
    name='pimg',
    version=__version__,
    description='Save an image in clipboard',
    description_content_type='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/eggplants/pimg',
    author='eggplants',
    packages=find_packages(),
    python_requires='>=3.5',
    include_package_data=True,
    license='MIT',
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            'pimg=pimg.main:main'
        ]
    }
)
