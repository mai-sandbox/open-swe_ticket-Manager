from typing import TypedDict

from langchain.chat_models import init_chat_model

class State(TypedDict):
    ticket_text: str
    category: str
    priority: str
    summary: str
    email: str
    acknowledgement: str

# Initialize the LLM model
llm = init_chat_model("openai:gpt-4.1")

def classify_ticket(state: State) -> dict:
    """
    Classify the ticket_text into 'Billing', 'Technical', or 'General Inquiry'.
    """
    # Use the LLM to classify the ticket text
    response = llm.invoke(state["ticket_text"])
    # For simplicity, assume the response directly provides the category
    category = response.get("category", "General Inquiry")
    return {"category": category}

def detect_priority(state: State) -> dict:
    """
    Detect the priority of the ticket_text as 'Low', 'Medium', or 'High'.
    """
    # Use the LLM to detect priority
    response = llm.invoke(state["ticket_text"])
    # For simplicity, assume the response directly provides the priority
    priority = response.get("priority", "Low")
    return {"priority": priority}


from langchain.chat_models import init_chat_model

class State(TypedDict):
    ticket_text: str
    category: str
    priority: str
    summary: str
    email: str
    acknowledgement: str

# Initialize the LLM model
llm = init_chat_model("openai:gpt-4.1")

def classify_ticket(state: State) -> dict:
    """
    Classify the ticket_text into 'Billing', 'Technical', or 'General Inquiry'.
    """
    # Use the LLM to classify the ticket text
    response = llm.invoke(state["ticket_text"])
    # For simplicity, assume the response directly provides the category
    category = response.get("category", "General Inquiry")
    return {"category": category}


class State(TypedDict):
    ticket_text: str
    category: str
    priority: str
    summary: str
    email: str
    acknowledgement: str




