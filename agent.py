from typing import Annotated

from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI
from typing_extensions import TypedDict

from langgraph.graph.message import add_messages


CLASSIFICATION_PROMPT = """You are a support agent. Classify the following ticket into one of the following categories:
Billing
Technical
General Inquiry

TICKET:
{ticket}

CLASSIFICATION:"""

PRIORITY_PROMPT = """You are a support agent. Determine the priority of the following ticket based on its content.
The priority can be Low, Medium, or High.

TICKET:
{ticket}

PRIORITY:"""


class State(TypedDict):
    messages: Annotated[list, add_messages]
    category: str
    priority: str
    summary: str
    route_to_email: str


def classify_ticket(state: State) -> dict:
    ticket = state["messages"][0].content
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    prompt = CLASSIFICATION_PROMPT.format(ticket=ticket)
    response = llm.invoke(prompt)
    category = response.content.strip()
    return {"category": category}


def detect_priority(state: State) -> dict:
    ticket = state["messages"][0].content
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    prompt = PRIORITY_PROMPT.format(ticket=ticket)
    response = llm.invoke(prompt)
    priority = response.content.strip()
    return {"priority": priority}


