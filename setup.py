import os

import pkg_resources
from setuptools import setup, find_packages

module = __import__('bitget')

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(
    name='bitget',
    version=module.__version__,
    keywords='bitget',
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    python_requires='>=3.6',
    extras_require={},
)
