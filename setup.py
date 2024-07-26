from setuptools import setup,find_packages


setup(
    name="End-to-end-ML-Project-with-MLflow",
    version='0.0.1',
    author='Akash',
    author_email='akashmukherjee0000@gmail.com',
     description="A small python package for ml app",
    package_dir={"": "src"},
    packages=find_packages(where="src")
)

