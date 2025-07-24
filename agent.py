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

def summarize_ticket(state: State) -> dict:
    """
    Generate a one-sentence summary of the ticket_text.
    """
    # Use the LLM to generate a summary
    response = llm.invoke(state["ticket_text"])
    # For simplicity, assume the response directly provides the summary
    summary = response.get("summary", "No summary available.")
    return {"summary": summary}

def route_ticket(state: State) -> dict:
    """
    Route the ticket based on category and priority.
    """
    category = state.get("category", "General Inquiry")
    priority = state.get("priority", "Low")
    
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
    else:
        email = "support@company.com"
    
    return {"email": email}

def draft_ack(state: State) -> dict:
    """
    Generate a 1-2 sentence acknowledgement email snippet referencing the summary and routing.
    """
    summary = state.get("summary", "No summary available.")
    email = state.get("email", "support@company.com")
    
    acknowledgement = f"Thank you for reaching out. We have categorized your request as: {summary}. Our team will get back to you via {email}."
    return {"acknowledgement": acknowledgement}


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

def summarize_ticket(state: State) -> dict:
    """
    Generate a one-sentence summary of the ticket_text.
    """
    # Use the LLM to generate a summary
    response = llm.invoke(state["ticket_text"])
    # For simplicity, assume the response directly provides the summary
    summary = response.get("summary", "No summary available.")
    return {"summary": summary}

def route_ticket(state: State) -> dict:
    """
    Route the ticket based on category and priority.
    """
    category = state.get("category", "General Inquiry")
    priority = state.get("priority", "Low")
    
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
    else:
        email = "support@company.com"
    
    return {"email": email}


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

def summarize_ticket(state: State) -> dict:
    """
    Generate a one-sentence summary of the ticket_text.
    """
    # Use the LLM to generate a summary
    response = llm.invoke(state["ticket_text"])
    # For simplicity, assume the response directly provides the summary
    summary = response.get("summary", "No summary available.")
    return {"summary": summary}


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







