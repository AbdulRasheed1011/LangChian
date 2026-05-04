from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

"""
from tavily import TavilyClient
tavily = TavilyClient()

@tool
def search(query: str) -> str:

    Tool that search over internet
    Args: 
        The query to search
    result:
        The search result
    
    print(f"Search for {query}")
    return tavily.search(query = query)
"""

llm  = ChatOpenAI(model = "gpt-5")
tools = [TavilySearch()]
agent = create_agent(model = llm, tools = tools)
def main():
    print("Hello from langchain!")
    result = agent.invoke({"messages":HumanMessage(content= "search 3 jobs for AI Engineering using LangChain in DFW, Texas on Linkdein and list their details.")})
    print(result)
if __name__ == "__main__":
    main()
