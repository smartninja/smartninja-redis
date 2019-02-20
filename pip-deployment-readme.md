# Steps for deploying to Pypi

1. Create a Python 3 virtual environment.
2. Change the package version number in `setup.py`.
3. Install setuptools and wheel: `pip install --upgrade setuptools wheel twine`
4. Run setup.py: `python setup.py sdist`
5. Upload via Twine: `twine upload dist/*`
