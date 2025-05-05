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
        WikipediaTools(),
        GoogleSearchTools(),
        YFinanceTools(stock_price=True),
        CalculatorTools()
    ],
    model=Gemini(id="gemini-2.0-flash"),
    #instructions=["Always use tools. Always include sources"],
    #description="You are an assistant, please reply based on the question.",
    show_tool_calls=True,
    markdown=True,
    stream=True,
    debug_mode=False,
    )   
#web_agent.print_response("Who is the current president of the United States?")
#web_agent.print_response("What is the stock price of Microsoft and who is their CEO?")
#web_agent.print_response("What is the latest news on AI?")
#web_agent.print_response("What is 2^20?")
#web_agent.print_response("What is the total area of USA in square miles and then convert to square kilometers?")
web_agent.print_response("Who won the India vs New Zealand finals in CT Mar 2025", stream=True)
