from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq 
from openai import OpenAI


@CrewBase
class FinancialAnalystCrew():
    """Financial Analyst Crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        # Use Groq Cloud
        #self.groq_llm = ChatGroq(temperature=0, model_name="mixtral8x7b-3268")
        self.groq_llm = ChatGroq(temperature=0, model_name="llama3-8b-8192")
        
        # Chat with an intelligent assistant in your terminal
        # Point to the local server
        #self.groq_llm = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
        

    @agent
    def company_researcher(self) -> Agent:
        return Agent (
            config = self.agents_config['company_researcher'],
            llm = self.groq_llm
        )
    
    @agent
    def company_analyst(self) -> Agent:
        return Agent (
            config = self.agents_config['company_analyst'],
            llm = self.groq_llm
        )
    
    @task
    def company_research_task(self) -> Task:
        return Task (
            config = self.tasks_config['research_company_task'],
            agent = self.company_researcher()
        )
    
    @task
    def analyze_company_task(self) -> Task:
        return Task (
            config = self.tasks_config['analyze_company_task'],
            agent = self.company_analyst()
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the Financial Analyst Crew"""
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = 2
        )