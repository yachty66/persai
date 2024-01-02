from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='persai',
    version='0.0.1',
    packages=find_packages(),
    install_requires=required,
    description="Big Five Personality Analysis based on X posts.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Max Hager',
    author_email='maxhager28@gmail.com',
    url='https://github.com/yachty66/persai',
    include_package_data=True
)
