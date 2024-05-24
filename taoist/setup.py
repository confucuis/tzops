# 项目打包成可执行程序
# python3 setup.py bdist_wheel
from setuptools import setup, find_packages

setup(
    name="taoist",
    version="0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "taoist = taoist.main:main"
        ]
    },
)

