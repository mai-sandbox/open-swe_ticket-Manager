# Support‑Ticket Triage Agent

This repository contains a LangGraph agent for automatically processing customer support tickets.

## Features

1. **Classification** (`classify_ticket`)  
   Uses an LLM to bucket tickets into Billing, Technical, or General Inquiry.  
2. **Priority Detection** (`detect_priority`)  
   Uses an LLM to tag each ticket as Low, Medium, or High urgency.  
3. **Summarization** (`summarize_ticket`)  
   Generates a one‑sentence summary of the ticket.  
4. **Routing** (`route_ticket`)  
   Maps `(category, priority)` to the correct email address.  
5. **Acknowledgement Draft** (`draft_ack`)  
   Writes a 1–2 sentence acknowledgement email snippet.

