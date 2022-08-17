from setuptools import setup, find_packages

requirements = [
    "flask==1.1.2",
    "waitress>=2.1.1",
    "click==7.1.2",
    "wtforms==2.3.3",
    "flask-wtf==0.14.3",
    "flask-bootstrap==3.3.7.1",
    "google-cloud-storage==1.30.0",
]

test_requirements = [
    "pytest==6.0.1",
    "pytest-cov==2.10.1",
    "pylint==2.5.3",
    "pytype==2020.8.10",
    "flake8==3.8.3",
    "black==19.10b0",
]

setup(
    name="opening-hours",
    version="0.1",
    description="Convert dates/times into human readable messages",
    url="woltchallenge.app",
    author="Michael Tanner",
    author_email="tanner.mbt@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    tests_require=requirements + test_requirements,
    extras_require={"test": requirements + test_requirements},
    python_requires=">=3.7",
    entry_points={"console_scripts": ["run_svc=src.app.service:start_serving"]},
)
