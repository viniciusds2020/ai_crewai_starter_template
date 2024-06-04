### Sistemas de multi-agentes de inteligencias artificiais

# Biblioteca
from crewai_tools import tool
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun

# Modelo LLM - Llama3 70B
llm = ChatGroq(temperature=0.7,
               groq_api_key='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',
               model_name='llama3-70b-8192')

# Ferramentas - Busca na internet com DuckDuckGo
@tool('DuckDuckGoSearchRun')
def search_tool(search_query: str):
  ''' Search the web for infotmation on a given topic'''
  return DuckDuckGoSearchRun().run(search_query)

# Topico do blog
topic = "Apple"

# Agentes
researcher = Agent(
    role = "Senior Researcher",
    goal = f"Explore trending technologies in {topic}.",
    backstory = "You are an innovative researher who follows the latest technology",
    verbose = True,
    tools = [search_tool],
    llm = llm,
)

writer = Agent(
    role = "Top Writer",
    goal = f"Create engaging content about {topic}. ",
    backstory = "You are an expert blogger who writes interesting articles.",
    verbose = True,
    tools = [search_tool],
    llm = llm,
)

# Tarefas
research_task = Task(
    description = f"Investigate the latest AI trends in {topic}.",
    expected_output = "A comprehensive 4 paragraphs long report on the latest AI trends.",
    tools = [search_tool],
    agent = researcher,
)

write_task = Task(
    description = f"Write an engaging article on {topic} that focuses on the latest trends.",
    expected_output = f"A comprehensive 4 paragraphs blog on {topic} in markdown format.",
    tools = [search_tool],
    agent = researcher,
    output_file = "my-blog.md"
)

# Orquestrador
crew = Crew(
    agents=[researcher, writer],
    tasks = [research_task, write_task]
)

result = crew.kickoff(
    inputs = {"topic": "AI in finance"}
)
