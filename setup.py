import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Amazon-Automatic-Web-Scrapper"
AUTHOR_USER_NAME = "Nik-Nikhil1910"
SRC_REPO = "amazonenv"
AUTHOR_EMAIL = "nikhilkondinya@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author="Nikhil Sharma",
    author_email="nikhilkondinya@gmail.com",
    description="Automatic web scrapper for amazon",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/Nik-Nikhil1910/Amazon-Automatic-Web-Scrapper.git",
    project_urls={
        "Bug Tracker": f"https://github.com/Nik-Nikhil1910/Amazon-Automatic-Web-Scrapper/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)