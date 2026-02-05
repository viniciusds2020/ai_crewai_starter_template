# Agentes de IA com CrewAI e Llama3 usando a API Groq

Este repositório contém um exemplo de como criar agentes de IA usando a biblioteca CrewAI, o modelo Llama3 e a API Groq em Python.

## Requisitos

- Python 3.8+
- Conta na Groq e chave de API

## Instalação

```bash
git clone https://github.com/viniciusds2020/ai_crewai_starter_template.git
cd ai_crewai_starter_template
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` (ou exporte no shell) com sua chave:

```ini
GROQ_API_KEY=your_api_key_here
```

## Uso

```bash
python main.py
```

Saída principal:
- Relatório de pesquisa gerado pelo agente pesquisador.
- Artigo salvo em `my-blog.md`, gerado pelo agente escritor.

## Estrutura

```plaintext
.
├── README.md
├── requirements.txt
└── main.py
```

## Revisão aplicada neste template

- Remoção de chave de API hardcoded no código.
- Ajuste de responsabilidade de tarefas (agente escritor escreve o blog).
- Pequenos ajustes de qualidade (função `main`, docstrings e mensagens de erro).
