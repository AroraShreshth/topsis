from setuptools import setup
def readme():
    with open('README.md') as f:
        README = f.read()
    return README
setup(
  name = 'topsis-shreshth-101803503',        
  packages = ['topsis-shreshth-101803503'],   
  version = '0.1',    
  license='MIT',      
  description = 'TOPSIS implementation via pandas',   
  long_description=readme(),
  long_description_content_type="text/markdown",
  author = 'Shreshth Arora',                  
  author_email = 'pypi@shreshtharora.com',      
  url = 'https://github.com/AroraShreshth/topsis', 
  install_requires=[          
          'pandas',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)