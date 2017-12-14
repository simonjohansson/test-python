from setuptools import setup, find_packages
install_requires = []

tests_require = [
    'pytest',
    'Flask-Testing'
]

setup(
    name='ee-enroll-github',
    version="{}".format('dev'),
    packages=find_packages(exclude=['tests']),
    author='Engineering Enablement',
    author_email='??',
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=['pytest-runner'],
    url='https://github.com/springernature/ee-enroll-github',
    entry_points={'console_scripts': []},
)
