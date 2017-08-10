"""
AIML Bot implements an interpreter for AIML, the Artificial Intelligence
Markup Language developed by Dr. Richard Wallace of the A.L.I.C.E. Foundation.
It can be used to implement a conversational AI program.
"""

# Command to build:
from setuptools import setup
import glob

package_prefix = "Lib/site-packages/aiml_bot"

setup(
    name="AIML Bot",
    version="0.0",
    author="Cort Stratton",
    author_email="cort@cortstratton.org",
    maintainer="Aaron Hosford",
    maintainer_email="hosford42@gmail.com",
    description="An interpreter package for AIML, the Artificial Intelligence Markup Language",
    long_description=__doc__,
    url="https://github.com/hosford42/aiml_bot",
    platforms=["any"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Communications :: Chat",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],

    packages=["aiml_bot"],
    data_files=[
        (package_prefix, glob.glob("aiml_bot/*.aiml")),
        (package_prefix, glob.glob("*.txt")),
    ],
)
