from setuptools import setup, find_packages

setup(
    name="taoist",
    version="0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "taoist = taoist.__main__:main"
        ]
    },
)

