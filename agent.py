from typing import TypedDict

class State(TypedDict):
    ticket_text: str
    category: str
    priority: str
    summary: str
    email: str
    acknowledgement: str


