from setuptools import setup

setup(
    name="flask-init",
    version="1.0",
    py_modules=["flask_init"],
    entry_points={
        "console_scripts": [
            "flask-init=flask_init:main"
        ]
    },
)
