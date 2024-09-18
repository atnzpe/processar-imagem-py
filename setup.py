from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_package",
    version="0.0.1",
    author="Gleyson Atanazio",
    author_email="gleysonasilva@gmail.com",
    description="Módulo para processamento e comparação de imagens.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atnzpe/processar-imagem-py",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)