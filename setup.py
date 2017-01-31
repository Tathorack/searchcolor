from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='image_search_colors',
      version='0.0.1',
      description='Image color extraction from web image search',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Other Audience',
        'Topic :: Artistic Software',
        'Topic :: Multimedia :: Graphics',
      ],
      keywords='image average color search google',
      url='',
      author='Rhys Hansen',
      author_email='rhyshonline@gmail.com',
      license='MIT',
      packages=['image_search_colors'],
      install_requires=[
          'google-api-python-client',
          'requests',
      ],
      include_package_data=True,
      zip_safe=False)
