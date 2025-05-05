from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    name="Finance Agent",
    model=Gemini(id="gemini-2.0-flash"),
    tools=[YFinanceTools(stock_price=True)],
    #instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
    debug_mode=False,
    stream=True,
)

agent.print_response("What is the stock price of NVDA and TSLA", stream=True)