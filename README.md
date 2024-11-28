# ETL Excel

![Fluxo](docs/static/fluxo.png)

## Sobre o Projeto

Esse repositório tem como objetivo o estudo e servir como portfolio. O intuito aqui é fornecer uma base e uma estrutura padronizada para iniciar projetos de engenharia, ciência e análise de dados. O foco principal é em boas práticas, automação, testes e documentação.

Este projeto é inspirado nos ensinamentos de Luciano Filho, cujo perfil no GitHub pode ser encontrado [aqui](https://github.com/lvgalvao). Ele forneceu a base do projeto, insights valiosos em suas aulas e suas contribuições para minha carreira na área de dados foram fundamentais para moldar minha base na área.

### Objetivos do Projeto

* **Entender a estrutura padrão de projetos**: Isso inclui a organização de diretórios, como o código-fonte, testes, documentação, entre outros.

* **Estruturas padrões em projetos de dados**: Vamos refatorar o projeto utilizando classes, módulos e boas práticas em uma ETL.

* **Familiarizar-se com ferramentas de desenvolvimento**: Abordaremos o uso de ambientes virtuais e discutiremos ferramentas como PIP, CONDA e POETRY.

* **Testes com Pytest**: Garanta que seu código funcione como esperado, criando testes unitários e de integração.

* **Versionamento com Git e GitHub**: Aprenda a versionar seu projeto e a usar o GitHub para colaboração e publicação.

* **Documentação com MKDocs**: Você vai aprender a documentar seu projeto com MKDocs e a publicar sua documentação no [GitHub Pages](rafaeljurkfitz.github.io/etl-excel/)

* **Automatização e CI/CD**: Configurar rotinas de integração e entrega contínua para manter a qualidade do projeto.

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

* **Luciano Filho** - [lvgalvaofilho@gmail.com](mailto:lvgalvaofilho@gmail.com)

* **Rafael Jurkfitz** - [rafaeljurkfitz@hotmail.com](mailto:rafaeljurkfitz@hotmail.com)
