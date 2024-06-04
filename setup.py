from setuptools import setup, find_packages

setup(
    name='KevDev.function_creator',
    version='0.1',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'sympy',
        'numpy',
    ],
    author='Kevin Milli',
    author_email='millikevin2@gmail.com',
    description='A package for creating and manipulating mathematical functions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Kevin-Milli/Function_Creator/tree/master',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
