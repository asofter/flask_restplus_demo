from setuptools import setup, find_packages

setup(
    name='REST_Demo',
    version='0.1',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask', 'flask-restplus',
        'flask-sqlalchemy', 'flask-cors',
        'Flask-Migrate', 'mysqlclient',
        'flask-jwt-extended', 'Flask-Bcrypt']
)