from setuptools import setup

setup(name='oleh_module_lib',
      version='2.1',
      description='What the oleh_module_lib does',
      url='https://github.com/username/repo',
      author='Your Name',
      author_email='email@domain.net',
      license='MIT',
      packages=['oleh_module_lib'],
      package_data={'oleh_module_lib': ['model.json', 'model.h5']},
      install_requires=[
                        # 'numpy>=1.19.0',
                        # 'tensorflow>=2.3.0',
                        # 'keras>=2.4'
                        # ,'importlib-resources>=3.3.0'
                        # ,'pillow>=8.0'
                        # ,'h5py>=3.1.0'
                        ],
      include_package_data=True)