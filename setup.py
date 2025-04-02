from setuptools import setup, find_packages

setup(
    name="fanpu_web_auto_test",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "selenium",
        "pytest",
        "faker",
    ],
)
