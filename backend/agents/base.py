from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

llm = ChatAnthropic(model="claude-3-opus-20241217")

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str    
    sources: list[str]
    tools_used: list[str]

parser = PydanticOutputParser(pydantic_object=ResearchResponse)


prompt = ChatPromptTemplate.from_messages([
    ("system", 
     """
     You are a research assistant that will generate a research paper.
    Answer the user query and use necessary tools.
    Wrap the output in this format and provide no other text\n{format_instructions}
    """,
    ),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}")
]).partial(format_instructions=parser.get_format_instructions())
