from setuptools import setup

setup(name='PinMol',
      version='beta',
      description='Find molecular beacons for live cell imaging of mRNAs',
      url='https://github.com/icatrina/PinMol_Win',
      author='Irina E. Catrina',
      author_email='iecatrina@gmail.com',
      license='Hunter College',
      #packages=['PinMol_Win'],
      install_requires=[
          'pandas<0.19', 'Biopython'],


      zip_safe=False,
      platforms=['any'])
