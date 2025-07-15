"""LangGraph Support Ticket Triage Agent"""

from typing import TypedDict
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END


class TicketState(TypedDict):
    """State schema for the support ticket triage workflow"""
    ticket_text: str
    category: str
    priority: str
    summary: str
    routed_email: str
    acknowledgement: str


# Initialize LLM for use across nodes
llm = init_chat_model("openai:gpt-4o-mini")


# Node function placeholders - will be implemented in subsequent tasks
def classify_ticket(state: TicketState) -> dict:
    """Classify ticket into Billing, Technical, or General Inquiry"""
    pass


def detect_priority(state: TicketState) -> dict:
    """Detect priority as Low, Medium, or High"""
    pass


# Create StateGraph instance
graph_builder = StateGraph(TicketState)


