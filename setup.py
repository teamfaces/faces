from distutils.core import setup

setup(
  name = 'faces',
  packages = ['faces'],
  version = '0.1',
  license='MIT',
  description = 'A Python library for developing desktop apps',
  author = 'Ricardo Gomes',
  author_email = 'desk467@gmail.com',
  url = 'https://github.com/teamfaces/faces',
  download_url = 'https://github.com/teamfaces/faces/archive/v_01.tar.gz',
  keywords = ['gui', 'desktop-apps', 'mobile'],
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