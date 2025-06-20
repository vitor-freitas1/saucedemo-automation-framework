[![Run Selenium Tests](https://github.com/vitor-freitas1/saucedemo-automation-framework/actions/workflows/run-tests.yml/badge.svg)](https://github.com/vitor-freitas1/saucedemo-automation-framework/actions/workflows/run-tests.yml)
# Projeto de Automação de Testes com Selenium e Pytest

## 📖 Sobre o Projeto

Este repositório contém um framework de automação de testes web para o site de e-commerce [Sauce Demo](https://www.saucedemo.com/). 
O projeto foi desenvolvido como uma demonstração de habilidades em automação de testes, seguindo as melhores práticas do mercado, incluindo o padrão Page Object Model (POM), execução de testes com Pytest e integração contínua com GitHub Actions.

Os cenários de teste cobrem as funcionalidades críticas da aplicação, como:
* Fluxos de login (válido e inválido).
* Adição de produtos ao carrinho de compras.
* Fluxo de checkout de ponta a ponta.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.13+
* **Automação de UI:** Selenium
* **Framework de Testes:** Pytest
* **Gerenciador de WebDriver:** webdriver-manager
* **CI/CD:** GitHub Actions

---

## 🏗️ Estrutura do Projeto

O projeto utiliza o padrão **Page Object Model (POM)** para garantir um código limpo, de fácil manutenção e reutilizável.

* `pages/`: Contém as classes que mapeiam as páginas da aplicação e suas ações (ex: `LoginPage`, `HomePage`).
* `tests/`: Contém os arquivos de teste escritos com Pytest.
* `conftest.py`: Arquivo de configuração central do Pytest, onde a fixture do `WebDriver` é gerenciada.
* `pytest.ini`: Arquivo de configuração para os marcadores do Pytest.
* `.github/workflows/`: Contém o workflow de CI/CD para execução automática dos testes.

---

## 🚀 Como Configurar e Rodar os Testes

Siga os passos abaixo para executar o projeto localmente.

### Pré-requisitos
* Python 3.13 ou superior instalado.
* Git instalado.

### Passos

1.  **Clone o repositório:**
    ```sh
    git clone https://github.com/vitor-freitas1/saucedemo-automation-framework.git
    cd saucedemo-automation-framework
    ```

2.  **Crie e ative um ambiente virtual:**
    ```sh
    # Criar ambiente virtual
    python -m venv .venv

    # Ativar no Windows
    .\.venv\Scripts\activate

    # Ativar no Linux/macOS
    source .venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Execute os testes:**
    ```sh
    # Para rodar todos os testes
    pytest

    # Para rodar apenas os testes de login
    pytest -m login

    # Para rodar apenas os testes de smoke
    pytest -m smoke
    ```

---