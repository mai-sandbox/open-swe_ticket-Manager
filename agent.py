from typing import Annotated

from langchain_core.messages import AIMessage, BaseMessage
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

SUMMARY_PROMPT = """You are a support agent. Summarize the following ticket in one sentence.

TICKET:
{ticket}

SUMMARY:"""

DRAFT_ACK_PROMPT = """You are a support agent. Draft a 1-2 sentence acknowledgement email snippet.
Reference the summary of the ticket and the email it was routed to.

SUMMARY: {summary}
ROUTED TO: {route_to_email}

ACKNOWLEDGEMENT:"""


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


def summarize_ticket(state: State) -> dict:
    ticket = state["messages"][0].content
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    prompt = SUMMARY_PROMPT.format(ticket=ticket)
    response = llm.invoke(prompt)
    summary = response.content.strip()
    return {"summary": summary}


def route_ticket(state: State) -> dict:
    category = state.get("category")
    priority = state.get("priority")

    if category == "Billing":
        if priority == "High":
            route_to_email = "priority-billing@company.com"
        else:
            route_to_email = "billing@company.com"
    elif category == "Technical":
        if priority == "High":
            route_to_email = "urgent-tech@company.com"
        else:
            route_to_email = "tech@company.com"
    else:
        route_to_email = "support@company.com"

    return {"route_to_email": route_to_email}


def draft_ack(state: State) -> dict:
    summary = state.get("summary")
    route_to_email = state.get("route_to_email")
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    prompt = DRAFT_ACK_PROMPT.format(summary=summary, route_to_email=route_to_email)
    response = llm.invoke(prompt)
    ack = AIMessage(content=response.content.strip())
    return {"messages": [ack]}





