# ETL Excel

![Fluxo](docs/static/fluxo.png)

## Sobre o Projeto

This repository is for studying and serving as a portfolio. The goal here is to have a standardized foundation and structure for starting engineering, science, and data analysis projects. The main focus is on best practices, automation, testing and documentation.

### Project objectives

* **Understand the standard project structure**: This includes organizing directories, such as source code, tests, documentation, among others.

* **Standard structures in data projects**: We will refactor the project using classes, modules and best practices in an ETL.

* **Become familiar with development tools**: We will cover the use of virtual environments and discuss tools such as PIP, CONDA and POETRY.

* **Tests with Pytest**: Ensure your code works as expected by creating unit and integration tests.

* **Versioning with Git and GitHub**: Learn how to version your project and use GitHub for collaboration and publishing.

* **Documentation with MKDocs**: You will learn how to document your project with MKDocs and publish your documentation on [GitHub Pages](rafaeljurkfitz.github.io/etl-excel/)

* **Automation and CI/CD**: Configure integration and continuous delivery routines to maintain project quality.

### Installation and Configuration

1. Clone the repository:

```bash
git clone https://github.com/rafaeljurkfitz/etl-excel.git
cd dataprojectstarterkit
```

2. Configure the correct Python version with `pyenv`::

```bash
pyenv install 3.12.1
pyenv local 3.12.1
```

3. Configure poetry for Python version 3.12.1 and activate the virtual environment:

```bash
poetry env use 3.12.1
poetry shell
```

4. Install the project dependencies:

```bash
poetry install
```

5. Run the tests to ensure everything is working as expected:

```bash
task test
```

6. Run the command to view the project documentation:

```bash
task doc
```

7. Run the pipeline execution command to perform the ETL:

```bash
task run
```

8. Check the ```data/output``` folder to see if the file was generated correctly.

## Contato

For questions, suggestions or feedback:

* **Rafael Jurkfitz** - [rafaeljurkfitz@hotmail.com](mailto:rafaeljurkfitz@hotmail.com)
