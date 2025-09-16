from setuptools import setup

setup(
    name="saxion",
    version="1.0",
    py_modules=["saxion_style"],
    entry_points={
        "pygments.styles": [
            "saxion = saxion_style:SaxionStyle",
        ],
    },
)
