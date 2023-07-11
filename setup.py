import setuptools

setuptools.setup(
    name="proxifier-cli",
    version="1.0.3",
    author="Pradish Bijukchhe",
    author_email="pradishbijukchhe@gmail.com",
    description="CLI to set up proxy configuration of Proxifier",
    url="https://github.com/sandbox-pokhara/proxifier-cli",
    project_urls={
        "Bug Tracker": "https://github.com/sandbox-pokhara/proxifier-cli/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3",
    include_package_data=True,
    package_data={"": ["proxifier_cli/*.ppx"]},
)
