# !/usr/bin/env python

from distutils.core import setup

setup(
    name="gitlab-ci-linter",
    packages=["gitlab_ci_linter"],
    version="1.0.0",
    description=".gitlab-ci.yml linter script",
    author="Alexey Burov",
    license="MIT",
    author_email="allburov@gmail.com",
    url="https://gitlab.com/devopshq/check-gitlab-ci",
    keywords=["linter", "gitlab",],
    python_requires=">=3.6",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development",
    ],
    entry_points={"console_scripts": ["gitlab-ci-linter=gitlab_ci_linter:main",]},
)
