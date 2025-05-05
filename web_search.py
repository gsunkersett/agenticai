from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.tools.wikipedia import WikipediaTools
# from phi.tools.google_search import GoogleSearch

web_agent = Agent(
    name="Web Agent",
    model=Gemini(id="gemini-2.0-flash"),
    tools=[WikipediaTools(), DuckDuckGo(), YFinanceTools(stock_price=True)],
    instructions=["Always use tools. Always include sources"],
    show_tool_calls=True,
    markdown=True,
)
web_agent.print_response("Who is the current president of the United States?", stream=True)
#web_agent.print_response("What time is it?", stream=True)