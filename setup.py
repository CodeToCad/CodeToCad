from setuptools import setup

from pathlib import Path
long_description = (Path(__file__).parent / "README.md").read_text()

setup(
    name='CodeToCAD',
    version='0.2.5',
    description='3D modeling automation in your favorite modeling software.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/CodeToCAD/CodeToCAD',
    author='CodeToCAD',
    author_email='shehab@codethatdown.com',
    license='GPL v3',
    packages=['CodeToCAD'],
    install_requires=[],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11"
    ],
)
