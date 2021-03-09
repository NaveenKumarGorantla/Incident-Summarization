from setuptools import setup, find_packages

setup(
	name='project0',
	version='1.0',
	author='Naveen Kumar Gorantla',
	author_email='Naveen.Kumar.Gorantla-1@ou.edu',
	packages=find_packages(exclude=('tests', 'docs')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']	
)
