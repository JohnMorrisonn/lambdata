del -r dist
del -r build
del -r lambdata_jjmorr13.egg-info

python setup.py sdist bdist_wheel
twine upload --repository-url https://test.pypi.org/legacy/ dist/*