1. Create artifact/library/package
python3 setup.py sdist bdist_wheel --universal

2. Upload/deploy the package
python3 -m twine upload --repository testpypi dist/*

3. Download package
pip install pneumonia_check==0.1 --extra-index-url=https://test.pypi.org/simple/
pip install -i https://test.pypi.org/simple/ pneumonia_check==0.1

0. file .pypirc
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = 

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = 