#!/bin/sh

/bin/rm dist/*
python3 setup.py sdist bdist_wheel
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

