from setuptools import setup, find_packages
#create a funtion to install dependancy from a requirements.txt file, this should take a file name and return a list of packages, ignore the # packages
def parse_requirements(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f if not line.startswith('#')]
#use the function to get the list of packages
setup(
    name='fianced-emission',
    version='0.1.0',
    author='Pratik',
    author_email='pratikpradhan64@gmail.com',
    description='Calculate financed emissions for banks as per the PCAF guidelines using the EEIO database',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/fianced-emission',
    packages=find_packages(),
    install_requires=["pymrio >= 0.5.4","streamlit >= 1.37.0","jupyterlab >= 4.2.4"], #parse_requirements('requirements.txt'),   #install the packages
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)