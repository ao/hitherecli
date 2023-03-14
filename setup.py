
import setuptools

setuptools.setup(
    name='hitherecli',  
    version='0.1',
    author="Andrew O",
    author_email="support@ataiva.com",
    description="Saying hi from the cli",
    long_description="Saying hi from the cli",
    url="https://github.com/ao/hitherecli",
    packages=["hitherecli"],
    entry_points = {
        "console_scripts": ['hitherecli = hitherecli.hitherecli:main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
