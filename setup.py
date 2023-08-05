import setuptools

VERSION = "0.1.0"

NAME = "st_tmdb_connection"

INSTALL_REQUIRES = [
    "streamlit>=1.22",
    "requests",
    "themoviedb",
    "pandas"
]


setuptools.setup(
    name=NAME,
    version=VERSION,
    description="Streamlit Connection for Tmdb API.",
    url="https://github.com/rajuptvs/Tmdb-Connection",
    project_urls={
        "Source Code": "https://github.com/rajuptvs/Tmdb-Connection",
    },
    author="Sai Rama Raju Penmatsa",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=INSTALL_REQUIRES,
    packages=["st_tmdb_connection"]
)