# ETL Excel

![Fluxo](docs/static/fluxo.png)

## Sobre o Projeto 🗃️

Esse repositório tem como objetivo servir como portfolio. O intuito aqui é demonstrar beneficio de boas praticas de desenvolvimento de software na área de dados e uma estrutura padronizada para iniciar projetos de engenharia, ciência e análise de dados.

**O foco principal é em boas práticas, automação, testes e documentação.**

### Requisitos 🚧

Existem duas coisas que devem ser feitas antes de qualquer projeto Python:

- Controle de versionamento do Python.

- Gerenciamento de pacotes e ambientes virtuais;

#### Pyenv 🔖

O ```Pyenv``` permite gerenciar **múltiplas versões do Python no mesmo sistema**, garantindo que você possa usar a versão correta para cada projeto.

#### Poetry 📦

O ```Poetry``` é uma ferramenta que gerencia **dependências**, **ambientes virtuais** e empacotamento de projetos Python.

**Principais vantagens do Poetry:**

- Gerenciamento centralizado no arquivo ```pyproject.toml```.
- Criação automática de ambientes virtuais isolados.
- Fluxo de instalação simplificado.

**O Poetry utiliza automaticamente a versão do Python configurada no projeto localmente via Pyenv. Para garantir que as ferramentas funcionem juntas.**

### Dependências ➕

#### Dependências do Projeto 🔧

Essas são as dependências essenciais para a execução do projeto. Elas incluem as bibliotecas necessárias para manipular e processar os arquivos Excel.

- ```pandas```: Biblioteca para análise e manipulação de dados.
- ```openpyxl```: Biblioteca para ler e escrever arquivos Excel.

#### Dependencias de Desenvolvimento 💻

Essas dependências são necessárias durante o desenvolvimento do projeto, como ferramentas para formatação de código, linting, e automação de tarefas.

- ```taskipy```: Para a automação de tarefas como execução de scripts e testes.
- ```pre-commit```: Para configurar hooks de pré-commit para garantir que o código esteja em conformidade com as convenções do projeto.
- ```pip-audit```: Para auditar dependências e verificar vulnerabilidades.
- ```pydocstyle```: Para checar o estilo de documentação do código.
- ```blue```: Ferramenta para formatação de código no estilo Black.
- ```isort```: Para ordenar as importações de forma consistente.

#### Dependencias de Teste 🧪

Essas dependências são necessárias para rodar os testes do projeto, como o framework de testes e seus plugins.

- ```pytest```: Framework para escrita e execução de testes automatizados.

#### Dependencias de Documentação 📚

Essas dependências são usadas para gerar e servir a documentação do projeto. Elas incluem ferramentas para a construção de sites de documentação e a geração de conteúdo dinâmico.

- ```mkdocstrings-python```: Para renderizar docstrings Python na documentação gerada pelo MkDocs.
- ```pygments```: Para colorir e formatar o código na documentação.
- ```pymdown-extensions```: Extensões para o MkDocs, permitindo o uso de Markdown avançado.
- ```mkdocs-bootstrap386```: Tema Bootstrap para o MkDocs.
- ```mkdocs-material```: Tema Material para o MkDocs.
- ```mkdocs```: Ferramenta para criar sites de documentação com Markdown.

### Instalação e Configuração

1. Clone o repositório:

    ```bash
    git clone https://github.com/rafaeljurkfitz/etl-excel.git
    cd etl-excel
    ```

2. Configure a versão correta do Python no `pyenv`::

    ```bash
    pyenv install 3.12.0
    pyenv local 3.12.0
    ```

3. Configure o poetry para o Python versão 3.12.0 e ative o ambiente virtual:

    ```bash
    poetry env use 3.12.0
    poetry shell
    ```

4. Instale as dependêcias do projeto:

    ```bash
    poetry install
    ```

5. Rode os testes para verificar que tudo está correto e funcionando:

    ```bash
    task test
    ```

6. Rode o comando para ver a documentação do projeto:

    ```bash
    task doc
    ```

7. Inicie a execução da pipeline utilizando o comando para iniciar a ETL:

    ```bash
    task run
    ```

8. Cheque o caminho da pasta ```data/output``` para ver se o arquivo que foi gerado está correto.

## Contato

Para questões, sugestões ou feedbacks:

- **Rafael Jurkfitz** - [rjurkfitz@gmail.com](mailto:rjurkfitz@gmail.com)

## Licença

Este projeto está licenciado sob a MIT License.
