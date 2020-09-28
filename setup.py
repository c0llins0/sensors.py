import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-libsensors3",
    version="0.0.1",
    author="Pavel Rojtberg",
    author_email="mail@rojtberg.net",
    description="Python Bindings for libsensors3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paroj/sensors.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
