from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.tools.wikipedia import WikipediaTools
from phi.tools.googlesearch import GoogleSearch
from phi.tools.calculator import Calculator

web_agent = Agent(
    name="Web Agent",
    model=Gemini(id="gemini-2.0-flash"),
    tools=[GoogleSearch(), WikipediaTools(), DuckDuckGo(), YFinanceTools(stock_price=True), Calculator()],
    #instructions=["Always use tools. Always include sources"],
    show_tool_calls=True,
    markdown=True,
    stream=True,
    verbose=True,
    debug_mode=False,
    )   
#web_agent.print_response("Who is the current president of the United States?")
#web_agent.print_response("What is the stock price of Microsoft and who is their CEO?")
#web_agent.print_response("What is the latest news on AI?")
#web_agent.print_response("What is 2^20?")
web_agent.print_response("What is the total area of USA in square miles and then convert to square kilometers?")
