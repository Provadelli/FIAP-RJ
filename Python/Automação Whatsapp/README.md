# 📱 Automação de Mensagens no WhatsApp com Python

## Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de automatizar o envio de mensagens personalizadas pelo WhatsApp a partir de dados armazenados em uma planilha Excel.

A aplicação realiza a leitura dos dados dos clientes, gera mensagens dinâmicas e automatiza o processo de envio utilizando o WhatsApp Web, reduzindo tarefas repetitivas e aumentando a eficiência operacional.

---

## Funcionalidades

* Leitura automática de dados em planilhas Excel;
* Personalização de mensagens para cada contato;
* Abertura automática do WhatsApp Web;
* Envio automatizado de mensagens;
* Processamento em lote de múltiplos contatos;
* Registro de erros durante a execução;
* Estrutura simples e de fácil manutenção.

---

## Tecnologias Utilizadas

* Python 3
* OpenPyXL
* PyAutoGUI
* WebBrowser
* urllib.parse
* Time
* OS

---

## Estrutura dos Dados

A planilha utilizada deve conter as seguintes colunas:

| Nome  | Telefone      | Vencimento |
| ----- | ------------- | ---------- |
| João  | 5511999999999 | 10/06/2026 |
| Maria | 5511888888888 | 15/06/2026 |

---

## Como Funciona

1. O sistema abre a planilha Excel.
2. Os dados dos clientes são carregados.
3. Uma mensagem personalizada é criada para cada contato.
4. O WhatsApp Web é aberto automaticamente.
5. A mensagem é enviada para o destinatário correspondente.
6. Caso ocorra algum erro, o contato é registrado em um arquivo de log.

---

## Exemplo de Mensagem

```text
Olá João, seu boleto vence no dia 10/06/2026.
Favor realizar o pagamento através do link informado.
```

---

## Instalação

### Verifique se o Python está instalado

```bash
py --version
```

---

### Clone o repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

Acesse a pasta do projeto:

```bash
cd nome-do-repositorio
```

---

### Atualize o pip (opcional)

```bash
py -m pip install --upgrade pip
```

---

### Instale o OpenPyXL

Biblioteca utilizada para leitura e manipulação de planilhas Excel.

```bash
py -m pip install openpyxl
```

---

### Instale o PyAutoGUI

Biblioteca utilizada para automação de teclado e mouse.

```bash
py -m pip install pyautogui
```

---

### Bibliotecas nativas do Python

As bibliotecas abaixo já acompanham a instalação padrão do Python e não precisam ser instaladas:

```python
import webbrowser
from urllib.parse import quote
from time import sleep
import os
```

---

## Executando o Projeto

Certifique-se de que:

* O WhatsApp Web esteja acessível;
* O QR Code já tenha sido autenticado;
* A planilha Excel esteja na pasta do projeto;
* Os dados estejam preenchidos corretamente.

Execute:

```bash
py index.py
```

ou

```bash
python index.py
```

---

## Estrutura do Projeto

```text
📦 Automacao-WhatsApp
├── index.py
├── Cópia de clientes.xlsx
├── erros.csv
├── README.md
└── assets/
    └── screenshot.png
```

---

## \Objetivo Educacional

Este projeto foi desenvolvido para praticar conceitos de:

* Automação de processos;
* Manipulação de arquivos Excel;
* Integração entre aplicações;
* Tratamento de exceções;
* Programação em Python;
* Desenvolvimento de soluções voltadas para produtividade.

---

## Autor

Pedro Lucas Souza Provadelli

🎓 Estudante de Engenharia de Software - FIAP

🚀 Let's Rock the Future
