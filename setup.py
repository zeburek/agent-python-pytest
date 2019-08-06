import os

from setuptools import setup


def read_file(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


version = '1.0.5'
tar_url = 'https://github.com/reportportal/agent-python-pytest/tarball/1.0.3'

dependencies = [
    'git+https://github.com/reportportal/client-Python.git@3.2.2',
]

requirements = [
    'pytest>=3.0.7',
    'six>=1.10.0',
    'dill>=0.2.7.1',
]


setup(
    name='pytest-reportportal',
    version=version,
    description='Agent for Reporting results of tests to the Report Portal',
    long_description=read_file('README.rst'),
    long_description_content_type='text/markdown',
    author='Pavel Papou',
    author_email='SupportEPMC-TSTReportPortal@epam.com',
    url='https://github.com/reportportal/agent-python-pytest',
    download_url=tar_url,
    packages=['pytest_reportportal'],
    install_requires=requirements,
    dependency_links=dependencies,
    license='Apache 2.0',
    keywords=['testing', 'reporting', 'reportportal', 'pytest'],
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
        ],
    entry_points={
        'pytest11': [
            'pytest_reportportal = pytest_reportportal.plugin',
        ]
    },
)
