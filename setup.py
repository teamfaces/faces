import setuptools
from distutils.core import setup

version = f'0.4'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='faces',
    packages=['faces', 'faces.drawers'],
    version=version,
    license='MIT',
    description='A Python library for developing desktop apps in a reactive way',
    long_description=long_description,
    author='Ricardo Gomes',
    author_email='desk467@gmail.com',
    url='https://github.com/teamfaces/faces',
    download_url=f'https://github.com/teamfaces/faces/releases/download/v{version}/faces-{version}.tar.gz',
    keywords=['gui', 'desktop-apps', 'mobile'],
    install_requires=[
        'tinycss',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: User Interfaces',

        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
