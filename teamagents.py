from phi.agent import Agent
from phi.model.groq import Groq  # Groq with Llama models
from phi.tools.duckduckgo import DuckDuckGo  # For web search
from phi.tools.yfinance import YFinanceTools  # For financial data
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Web Agent: Uses a specific Llama model for web search
web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-specdec"),  # A different Llama model for the Web Agent
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

# Finance Agent: Uses a different Llama model for financial analysis
finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="llama-3.3-70b-versatile"),  # A specialized Llama model for financial tasks
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# Team Agent: Combines Web Agent and Finance Agent
agent_team = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),  # Coordinator could use another Llama model, if needed
    team=[web_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# Request information from the agent team
agent_team.print_response(
    "Summarize analyst recommendations and share the latest news for NVDA"
)
