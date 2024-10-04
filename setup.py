from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="my-image-processing",
    version="0.0.3",
    author="Petkovic Gonçalves de Almeida",
    author_email="petnugon@gmail.com",
    description="Image processing package using Skimage",
    long_description="page_description",
    long_description_content_type="text/markdown",
    url="https://github.com/Petkovicc/Criando-um-Pacote-de-Processamento-com-Python",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.5",
)