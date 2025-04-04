# agent/agent_runner.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo-1106")

# Define the search tool
search_tool = TavilySearchResults()

# Create the agent
agent_executor = create_react_agent(llm, tools=[search_tool])

# Test the agent
query = "Recent climate events affecting insurance in 2025"
response = agent_executor.invoke({"input": query})  # Note: changed "query" to "input"
print(response)