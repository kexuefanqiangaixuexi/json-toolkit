from setuptools import setup, find_packages

setup(name="json-toolkit", version="0.1.0", packages=find_packages(), entry_points={"console_scripts": ["json-pretty=json_toolkit.pretty:main", "json-diff=json_toolkit.diff:main", "json-query=json_toolkit.query:main"]})