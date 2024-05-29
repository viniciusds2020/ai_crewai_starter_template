# Agentes de IA com CrewAI e Llama3 usando a API Groq

Este repositório contém um exemplo de como criar agentes de IA usando a biblioteca CrewAI, o modelo Llama3 e a API Groq em Python. O objetivo é fornecer uma estrutura básica para configurar e executar agentes de IA.

## Requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados:

- Python 3.8 ou superior
- Biblioteca CrewAI
- Acesso à API Groq para o modelo Llama3
- pip para gerenciar pacotes Python

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/viniciusds2020/ai_crewai_starter_template.git
    cd ai_crewai_starter_template
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Configuração

1. Obtenha uma chave de API da Groq para acessar o modelo Llama3. Registre-se no site da Groq e siga as instruções para gerar a chave de API.

2. Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API:

    ```ini
    GROQ_API_KEY=your_api_key_here
    ```

## Uso

O arquivo principal `main.py` contém a lógica para inicializar e executar o agente de IA. Para iniciar o agente, execute:

```bash
python main.py
```

## Estrutura do Projeto

```plaintext
.
├── README.md
├── requirements.txt
├── main.py
└── .env
```

- `README.md`: Este arquivo de documentação.
- `requirements.txt`: Arquivo de dependências do Python.
- `main.py`: Script principal que inicializa e executa o agente de IA.
- `.env`: Arquivo contendo a chave de API da Groq.


## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorar este projeto.

## Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo LICENSE para mais detalhes.
