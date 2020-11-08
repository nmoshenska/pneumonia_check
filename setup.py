from setuptools import setup

setup(name='pneumonia_check',
      version='0.3',
      description='What the pneumonia_check does',
      url='https://github.com/nmoshenska/pneumonia_check',
      author='Nikol Moshenska',
      author_email='nmoshenska21@andover.edu',
      license='MIT',
      packages=['pneumonia_check'],
      package_data={'pneumonia_check': ['model.json', 'model.h5']},
      install_requires=[
                         'numpy<1.19.0',
                         'tensorflow>=2.3.0',
                         'keras>=2.4',
                         'importlib-resources>=3.3.0',
                         'pillow>=8.0',
                         'h5py<2.11.0'
                        ],
      include_package_data=True)