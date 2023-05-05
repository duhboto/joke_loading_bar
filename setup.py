from setuptools import setup, find_packages

setup(
    name='joke_loading_bar',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'rich>=10.4.0',
    ],
    include_package_data=True
)
