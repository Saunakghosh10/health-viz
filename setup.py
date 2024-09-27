from setuptools import setup, find_packages

setup(
    name="healthviz",  # This is the name of your package on PyPI
    version="0.1.0",  # Initial release version
    description="A package for health data visualization and analysis",
    long_description=open('README.md').read(),  # Use README for long description
    long_description_content_type='text/markdown',  # The type of README file
    url="https://github.com/Saunakghosh10",  # Replace with your GitHub repo link
    author="Your Name",
    author_email="your.email@example.com",
    license="MIT",  # Choose your license type
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=[  # List your package dependencies
        "pandas",
        "matplotlib",
        "seaborn",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
