from setuptools import find_packages, setup

setup(
    name="alfred-timebox",
    entry_points={
        "console_scripts": [
            "timebox-cached = timebox.commands.cached:main",
            "timebox-favorites = timebox.commands.favorites:main",
            "timebox-projects = timebox.commands.projects:main",
            "timebox-trigger = timebox.commands.trigger:main",
            "timebox-start = timebox.commands.start:main",
        ],
    },
)
