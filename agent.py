"""
LangGraph Support Ticket Triage Agent

This module implements a StateGraph for processing customer support tickets
through classification, priority detection, summarization, routing, and acknowledgement.
"""

from typing import Optional, Dict, Any
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


class TicketState(TypedDict):
    """State schema for the support ticket triage process."""
    ticket_text: str
    category: Optional[str]
    priority: Optional[str]
    summary: Optional[str]
    routing_email: Optional[str]
    acknowledgement: Optional[str]


# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)


def classify_ticket(state: TicketState) -> Dict[str, Any]:
    """Classify the ticket into Billing, Technical, or General Inquiry."""
    prompt = f"""
    Classify the following customer support ticket into one of these categories:
    - Billing
    - Technical
    - General Inquiry
    
    Ticket: {state['ticket_text']}
    
    Respond with only the category name.
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    category = response.content.strip()
    
    return {"category": category}


def detect_priority(state: TicketState) -> Dict[str, Any]:
    """Detect priority level as Low, Medium, or High based on urgency clues."""
    prompt = f"""
    Analyze the following customer support ticket and assign a priority level:
    - High: Urgent issues, system down, security concerns, angry customers
    - Medium: Important but not critical, moderate impact
    - Low: General questions, minor issues, feature requests
    
    Ticket: {state['ticket_text']}
    Category: {state['category']}
    
    Respond with only: Low, Medium, or High
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    priority = response.content.strip()
    
    return {"priority": priority}


def summarize_ticket(state: TicketState) -> Dict[str, Any]:
    """Generate a one-sentence summary of the ticket."""
    prompt = f"""
    Create a clear, concise one-sentence summary of this customer support ticket:
    
    Ticket: {state['ticket_text']}
    Category: {state['category']}
    Priority: {state['priority']}
    
    Provide only the summary sentence.
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    summary = response.content.strip()
    
    return {"summary": summary}


def route_ticket(state: TicketState) -> Dict[str, Any]:
    """Route ticket to correct email based on category and priority."""
    category = state['category']
    priority = state['priority']
    
    # Routing rules
    if category == "Billing":
        if priority == "High":
            routing_email = "priority-billing@company.com"
        else:
            routing_email = "billing@company.com"
    elif category == "Technical":
        if priority == "High":
            routing_email = "urgent-tech@company.com"
        else:
            routing_email = "tech@company.com"
    elif category == "General Inquiry":
        routing_email = "support@company.com"
    else:
        # Fallback for unexpected categories
        routing_email = "support@company.com"
    
    return {"routing_email": routing_email}


def draft_ack(state: TicketState) -> Dict[str, Any]:
    """Draft a 1-2 sentence acknowledgement email snippet."""
    prompt = f"""
    Draft a professional 1-2 sentence acknowledgement for this customer support ticket:
    
    Summary: {state['summary']}
    Routed to: {state['routing_email']}
    Category: {state['category']}
    Priority: {state['priority']}
    
    The acknowledgement should:
    - Thank the customer
    - Reference the summary
    - Mention it's been routed to the appropriate team
    - Be professional and concise
    
    Provide only the acknowledgement text.
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    acknowledgement = response.content.strip()
    
    return {"acknowledgement": acknowledgement}


# Initialize the StateGraph with the TicketState schema
graph_builder = StateGraph(TicketState)

# Add nodes to the graph
graph_builder.add_node("classify_ticket", classify_ticket)
graph_builder.add_node("detect_priority", detect_priority)
graph_builder.add_node("summarize_ticket", summarize_ticket)
graph_builder.add_node("route_ticket", route_ticket)
graph_builder.add_node("draft_ack", draft_ack)

# Add sequential edges
graph_builder.add_edge(START, "classify_ticket")
graph_builder.add_edge("classify_ticket", "detect_priority")
graph_builder.add_edge("detect_priority", "summarize_ticket")
graph_builder.add_edge("summarize_ticket", "route_ticket")
graph_builder.add_edge("route_ticket", "draft_ack")
graph_builder.add_edge("draft_ack", END)

# Compile the graph
compiled_graph = graph_builder.compile()
