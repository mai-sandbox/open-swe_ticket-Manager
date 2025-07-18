"""
LangGraph Support Ticket Triage Agent

This module implements a StateGraph-based workflow for processing customer support tickets
through classification, priority detection, summarization, routing, and acknowledgement generation.
"""

from typing import Optional
from typing_extensions import TypedDict

from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    """State schema for the ticket triage workflow."""
    ticket_text: str
    category: Optional[str]
    priority: Optional[str]
    summary: Optional[str]
    email: Optional[str]
    acknowledgement: Optional[str]


# Initialize the LLM
llm = init_chat_model("openai:gpt-4o-mini")


def classify_ticket(state: State) -> dict:
    """
    Classify the ticket into one of three categories: Billing, Technical, or General Inquiry.
    
    Args:
        state: Current state containing ticket_text
        
    Returns:
        Dictionary with category field updated
    """
    prompt = f"""
    Classify the following customer support ticket into one of these three categories:
    - Billing
    - Technical
    - General Inquiry
    
    Ticket: {state['ticket_text']}
    
    Respond with only the category name (Billing, Technical, or General Inquiry).
    """
    
    response = llm.invoke(prompt)
    content = response.content if isinstance(response.content, str) else str(response.content)
    category = content.strip()
    
    # Ensure valid category
    valid_categories = ["Billing", "Technical", "General Inquiry"]
    if category not in valid_categories:
        category = "General Inquiry"
    
    return {"category": category}


def detect_priority(state: State) -> dict:
    """
    Detect the priority level of the ticket based on urgency clues.
    
    Args:
        state: Current state containing ticket_text and category
        
    Returns:
        Dictionary with priority field updated
    """
    prompt = f"""
    Analyze the following customer support ticket and determine its priority level based on urgency clues.
    
    Category: {state['category']}
    Ticket: {state['ticket_text']}
    
    Priority levels:
    - High: Urgent issues, system down, critical problems, angry customers, revenue impact
    - Medium: Important but not critical, moderate impact, some urgency
    - Low: General questions, minor issues, no immediate impact
    
    Respond with only the priority level (High, Medium, or Low).
    """
    
    response = llm.invoke(prompt)
    content = response.content if isinstance(response.content, str) else str(response.content)
    priority = content.strip()
    
    # Ensure valid priority
    valid_priorities = ["High", "Medium", "Low"]
    if priority not in valid_priorities:
        priority = "Medium"
    
    return {"priority": priority}


def summarize_ticket(state: State) -> dict:
    """
    Generate a one-sentence summary of the ticket.
    
    Args:
        state: Current state containing ticket_text, category, and priority
        
    Returns:
        Dictionary with summary field updated
    """
    prompt = f"""
    Create a clear, concise one-sentence summary of this customer support ticket.
    
    Category: {state['category']}
    Priority: {state['priority']}
    Ticket: {state['ticket_text']}
    
    Provide only the summary sentence, no additional text.
    """
    
    response = llm.invoke(prompt)
    content = response.content if isinstance(response.content, str) else str(response.content)
    summary = content.strip()
    
    return {"summary": summary}


def route_ticket(state: State) -> dict:
    """
    Route the ticket to the appropriate email address based on category and priority.
    
    Args:
        state: Current state containing category and priority
        
    Returns:
        Dictionary with email field updated
    """
    category = state['category']
    priority = state['priority']
    
    # Apply routing rules
    if category == "Billing":
        if priority == "High":
            email = "priority-billing@company.com"
        else:
            email = "billing@company.com"
    elif category == "Technical":
        if priority == "High":
            email = "urgent-tech@company.com"
        else:
            email = "tech@company.com"
    else:  # General Inquiry
        email = "support@company.com"
    
    return {"email": email}


def draft_ack(state: State) -> dict:
    """
    Draft an acknowledgement email snippet referencing the summary and routing.
    
    Args:
        state: Current state containing summary and email
        
    Returns:
        Dictionary with acknowledgement field updated
    """
    prompt = f"""
    Draft a professional 1-2 sentence acknowledgement email snippet for a customer support ticket.
    
    Summary: {state['summary']}
    Routed to: {state['email']}
    
    The acknowledgement should:
    - Thank the customer for contacting support
    - Reference the ticket summary
    - Indicate it has been routed to the appropriate team
    
    Provide only the acknowledgement text, no additional formatting.
    """
    
    response = llm.invoke(prompt)
    content = response.content if isinstance(response.content, str) else str(response.content)
    acknowledgement = content.strip()
    
    return {"acknowledgement": acknowledgement}


# Build the StateGraph
graph_builder = StateGraph(State)

# Add nodes
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
graph = graph_builder.compile()

# Export the compiled graph as required
compiled_graph = graph


