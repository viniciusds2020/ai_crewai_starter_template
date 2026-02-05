"""Exemplo de sistema multiagente com CrewAI.

Melhorias aplicadas nesta revisão:
- Remove segredo hardcoded (chave Groq) e lê de variável de ambiente.
- Corrige a definição das tarefas para usar o agente escritor na etapa de escrita.
- Evita variáveis globais desnecessárias e centraliza execução em `main()`.
"""

from __future__ import annotations

import os

from crewai import Agent, Crew, Task
from crewai_tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_groq import ChatGroq


@tool("DuckDuckGoSearchRun")
def search_tool(search_query: str) -> str:
    """Search the web for information on a given topic."""
    return DuckDuckGoSearchRun().run(search_query)


def build_crew(topic: str) -> Crew:
    """Monta os agentes e tarefas para um tema informado."""
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise RuntimeError(
            "A variável de ambiente GROQ_API_KEY não foi definida. "
            "Configure-a antes de executar o script."
        )

    llm = ChatGroq(
        temperature=0.7,
        groq_api_key=groq_api_key,
        model_name="llama3-70b-8192",
    )

    researcher = Agent(
        role="Senior Researcher",
        goal=f"Explore trending technologies in {topic}.",
        backstory="You are an innovative researcher who follows the latest technology.",
        verbose=True,
        tools=[search_tool],
        llm=llm,
    )

    writer = Agent(
        role="Top Writer",
        goal=f"Create engaging content about {topic}.",
        backstory="You are an expert blogger who writes interesting articles.",
        verbose=True,
        tools=[search_tool],
        llm=llm,
    )

    research_task = Task(
        description=f"Investigate the latest AI trends in {topic}.",
        expected_output="A comprehensive 4-paragraph report on the latest AI trends.",
        tools=[search_tool],
        agent=researcher,
    )

    write_task = Task(
        description=f"Write an engaging article on {topic} that focuses on the latest trends.",
        expected_output=f"A comprehensive 4-paragraph blog on {topic} in markdown format.",
        tools=[search_tool],
        agent=writer,
        output_file="my-blog.md",
    )

    return Crew(agents=[researcher, writer], tasks=[research_task, write_task])


def main() -> None:
    topic = "AI in finance"
    crew = build_crew(topic)
    result = crew.kickoff(inputs={"topic": topic})
    print(result)


if __name__ == "__main__":
    main()
