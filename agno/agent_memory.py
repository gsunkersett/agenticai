from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.embedder.google import GeminiEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType

vector_db = LanceDb(
            uri="tmp/lancedb",
            table_name="recipes",
            search_type=SearchType.hybrid,
            embedder=GeminiEmbedder(
                id="gemini-embedding-exp-03-07",
            )
)
knowledgebase=PDFUrlKnowledgeBase(
        urls=[
            "https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf",
        ],
        vector_db=vector_db,
        )

agent = Agent(
    name="Knowledge Agent",
    model=Gemini(id="gemini-2.0-flash"),
    description="You are a Thai cuisine expert.",
    tools=[
        DuckDuckGoTools(),
    ],
    knowledge=knowledgebase,
    search_knowledge=True,
    instructions=["Search your knowledge base for recipes", " Always search your knowledge base first and use it of available", "If you don't find, use web search"],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
    stream=True,
)

agent.knowledge.load(recreate=False)

agent.print_response("Show me recipe for Thai Papaya Salad", stream=True)