from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from agno.tools.wikipedia import WikipediaTools
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.calculator import CalculatorTools

web_agent = Agent(
    name="Web Agent",
    role="web search agent",
    tools=[
        DuckDuckGoTools(),
    ],
    model=Gemini(id="gemini-2.0-flash"),
    #instructions=["Always use tools. Always include sources"],
    #description="You are an assistant, please reply based on the question.",
    show_tool_calls=True,
    markdown=True,
    stream=True,
    debug_mode=False,
    )   

finance_agent = Agent(
    name="Finance Agent",
    role="Finance agent",
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True),
        ],
    model=Gemini(id="gemini-2.0-flash"),
    instructions=["Use tables to show data. Show in depth analysis"],
    #description="You are an assistant, please reply based on the question.",
    show_tool_calls=True,
    markdown=True,
    stream=True,
    debug_mode=False,
    )  

agent_team = Agent(
    name="Agent Team",
    role="A team of agents working together",
    team = [web_agent, finance_agent],
    model=Gemini(id="gemini-2.0-flash"),
    instructions=["Always include sources", "Use tables to show data", "Show in depth analysis"],
    #description="You are an assistant, please reply based on the question.",
    show_tool_calls=True,
    markdown=True,
    stream=True,
    debug_mode=False, 
)
agent_team.print_response("Analyze companies like AAPL, MSFT, NVDA and suggest what stock to buy")
