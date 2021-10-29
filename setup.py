from setuptools import find_packages, setup

setup(
    name="nbss-upload",
    version="0.1",
    url="https://github.com/notebook-sharing-space/nbss-upload",
    description="Upload notebooks to a notebooksharing.space instance",
    license="3-clause BSD",
    author="Yuvi Panda",
    author_email="yuvipanda@gmail.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    py_modules=["nbss_upload"],
    entry_points = {
        'console_scripts': ['nbss-upload=nbss_upload:main'],
    },
    install_requires=["requests"],
    platforms="any",
    zip_safe=False,
)
