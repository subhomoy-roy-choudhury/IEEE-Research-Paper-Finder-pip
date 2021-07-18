from setuptools import setup
import pathlib

DESCRIPTION = "This is a command line tool to extract research paper details along with their download links with the help of keywords ."
# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="IEEE Research Paper Finder",
    version="0.0.1",
    description= DESCRIPTION,
    long_description = README,
    long_description_content_type="text/markdown",
    author="Subhomoy Roy Choudhury",
    author_email = "subhomoyrchoudhury@gmail.com",
    url="https://github.com/subhomoy-roy-choudhury/IEEE-Research-Paper-Finder-pip",
    license="MIT",
    classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
    packages=['research_paper_finder'],
    include_package_data=True,
    install_requires=['selenium','beautifulsoup4','chromedriver-autoinstaller','requests'],
    entry_points={
        "console_scripts": [
            "finder = research_paper_finder.finder:main",
        ]
    },
)