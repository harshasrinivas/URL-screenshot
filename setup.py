"""main installation setup file"""

from setuptools import setup

setup(name='url-screenshot',
      description='Get URL screenshots',
      version='0.1.0',
      author='Harsha Srinivas',
      author_email='95harsha95@gmail.com',
      packages=['url_screenshot'],
      entry_points={
          'console_scripts': ['url-screenshot=url_screenshot:main'],
      },
      url='https://github.com/harshasrinivas/url-screenshot/',
      keywords=['screenshot', 'CLI', 'python'],
      classifiers=[
          'Operating System :: POSIX',
          'Environment :: Console',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Topic :: Utilities',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],)
