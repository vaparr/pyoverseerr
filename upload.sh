rm -rf dist/
rm -rf build/
python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
/root/.local/bin/twine upload dist/*


