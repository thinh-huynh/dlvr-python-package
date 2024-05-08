import setuptools

setuptools.setup(
    name='dlvr_python_package',
    version='0.0.1',
    author='Thinh Huynh',
    author_email='thinh.huynh@deliveree.com',
    description='Deliveree python package',
    packages=['dlvr_database'],
    install_requires=[
        'SQLAlchemy==2.0.16',
        'sqlalchemy-utils==0.41.1',
        'asyncpg==0.28.0'
    ]
)
