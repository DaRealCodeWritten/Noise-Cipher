import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="noise-cipher",
    version="0.1.4",
    author="CodeWritten",
    author_email="ytcodew@gmail.com",
    description="A new cipher module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DaRealCodeWritten/Noise-Cipher",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
