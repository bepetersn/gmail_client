from setuptools import setup

setup(
    name = "gmail-client",
    version = "0.0.8.1",
    author = "Wilberto Morales",
    author_email = "wilbertomorales777@gmail.com",
    description = ("A Pythonic interface for Google Mail. Based of https://github.com/charlierguo/gmai"),
    license = "MIT",
    keywords = "google gmail client",
    url = "https://github.com/wilbertom/gmail",
    packages=['gmail_client', 'gmail_client.codecs'],
    classifiers=[
        "Topic :: Communications :: Email",
        "License :: OSI Approved :: MIT License",
    ],
)
