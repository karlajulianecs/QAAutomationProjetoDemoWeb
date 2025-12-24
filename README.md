# 🧪 Projeto QA Automation – Demo Web Shop

Projeto de automação de testes Web utilizando **Python + Selenium + Pytest**, aplicando o padrão **Page Object Model (POM)** com separação de **Elements** e **Pages**.


---
## 👥 Equipe do Projeto

Este projeto foi desenvolvido pela seguinte equipe de QA Automation:

Karla Chaves

Samira Jeovana

Raissa Menezes

---

## 🔧 Tecnologias Utilizadas

- Python 3.12
- Selenium WebDriver
- Pytest
- Allure Reports
- ChromeDriver

---

## 🧱 Arquitetura

- **elements/** → locators da aplicação
- **pages/** → regras de negócio e ações
- **tests/** → cenários de teste
- **utils/** → configuração do driver
- **reports/** → evidências (Allure)

---

## 🧪 Cenários Automatizados

| ID | Cenário |
|----|--------|
| CT001 | Adicionar produto ao carrinho |
| CT002 | Remover produto do carrinho |
| CT003 | Atualizar quantidade do produto |
| CT004 | Buscar produto existente |
| CT005 | Ordenar produtos por preço |
| CT006 | Adicionar produto à wishlist |
| CT007 | Estimar frete |
| CT008 | Comparar produtos |
| CT009 | Limpar carrinho |

---

## ▶️ Como Executar os Testes

```bash
pip install -r requirements.txt
pytest


ProjetoDemoWeb/
│
├── elements/                # Mapeamento de locators (Elementos da UI)
│   ├── HomeElements.py
│   ├── ProductElements.py
│   ├── CartElements.py
│   ├── SearchElements.py
│   ├── HeaderElements.py
│   └── CompareElements.py
│
├── pages/                   # Page Objects (Ações e comportamentos)
│   ├── BasePage.py
│   ├── HomePage.py
│   ├── ProductPage.py
│   ├── CartPage.py
│   ├── SearchPage.py
│   ├── ComparePage.py
│   └── HeaderComponent.py
│
├── tests/                   # Cenários de teste automatizados
│   ├── test_ct001_adicionar_produto_ao_carrinho.py
│   ├── test_ct002_remover_produto_do_carrinho.py
│   ├── test_ct003_atualizar_quantidade_produto.py
│   ├── test_ct004_buscar_produto_existente.py
│   ├── test_ct005_ordenar_produtos_por_preco.py
│   ├── test_ct006_adicionar_produto_a_wishlist.py
│   ├── test_ct007_estimar_frete.py
│   ├── test_ct008_comparar_produtos.py
│   └── test_ct009_limpar_carrinho.py
│
├── utils/
│   └── driver_factory.py    # Fábrica de drivers (Chrome, Firefox, etc.)
│
├── reports/
│   └── allure-results/      # Evidências para relatório Allure
│
├── conftest.py              # Fixtures globais (driver, browser)
├── pytest.ini               # Configurações do Pytest
├── requirements.txt         # Dependências do projeto
└── README.md                # Documentação do projeto
