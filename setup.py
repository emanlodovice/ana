from setuptools import setup, find_packages

setup(
    name='django-ana',
    version='0.0.1',
    description='An analytics django application',
    long_description=open('README.md').read(),
    packages=find_packages(),
    python_requires='~=3.6',
    url='https://github.com/emanlodovice/ana',
    license='MIT',
    author='Emmanuel Lodovice',
    author_email='name3anad@gmail.com',
    keywords=['django', 'analytics', 'ana']
)
