# Agent Instructions for Python LangGraph Development

## General Rules

- Always use proper Python package management with `pip` and `requirements.txt`
- Include comprehensive type hints throughout the codebase - this is critical for LangGraph applications
- Follow PEP 8 style guidelines and maintain consistent code formatting
- Use proper error handling and logging instead of simple print statements
- Always run code quality checks (`ruff` and `mypy`) before considering implementation complete
- Follow existing code patterns and maintain consistency with established LangGraph architecture
- Keep inline comments minimal - prefer clear, self-documenting code
- Ensure all LangGraph applications compile successfully with proper state management

## Python Project Structure

Standard LangGraph Python project structure:

```
project_name/
├── main.py               # Main LangGraph implementation (or agent.py, app.py)
├── tools.py              # Tool implementations (if using tools)
├── state.py              # State schema definitions (if complex)
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variable template
└── README.md             # Project documentation
```

**Naming Conventions**:
- Use descriptive names for your main file (`agent.py`, `chatbot.py`, `workflow.py`, etc.)
- Group related functionality in appropriately named modules
- Follow Python module naming conventions (lowercase with underscores)

## Dependencies and Installation

**Package Manager**: Use `pip` with virtual environments

**Installation Process**:
- Create virtual environment: `python -m venv venv`
- Activate environment: `source venv/bin/activate` (Unix) or `venv\Scripts\activate` (Windows)
- Install dependencies: `pip install -r requirements.txt`

**Key Dependencies for LangGraph Projects**:
- Core LangGraph: `langgraph>=0.2.0`
- LangChain ecosystem: `langchain>=0.2.0`, `langchain-anthropic>=0.1.0` (or other LLM providers)
- Development tools: `ruff>=0.1.0`, `mypy>=1.7.0`
- Environment management: `python-dotenv>=1.0.0`
- Additional libraries as needed for your specific use case (tools, APIs, etc.)

**Requirements Management**: All dependencies must be properly specified in `requirements.txt` with appropriate version constraints.

## Code Quality Requirements

**Mandatory Code Quality Checks**:

1. **Ruff Linting**: Run `ruff check .` to validate code quality
   - Checks syntax, style, imports, and common Python issues
   - Must pass without errors before submission
   - Fix issues with `ruff check . --fix` when possible

2. **MyPy Type Checking**: Run `mypy . --ignore-missing-imports` for type validation
   - Critical for LangGraph state management and tool integration
   - Ensures proper TypedDict usage and function signatures
   - Must pass without type errors

**Running Quality Checks**:
```bash
# Check code quality
ruff check .

# Fix auto-fixable issues
ruff check . --fix

# Type checking
mypy . --ignore-missing-imports

# Format code (if using ruff format)
ruff format .
```

## LangGraph Specific Requirements

**State Management**:
- Use proper TypedDict definitions with correct annotations
- Always use `Annotated[list, add_messages]` for message handling
- Include comprehensive type hints for all state fields

Example:
```python
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    # Other state fields with proper types
```

**Graph Implementation**:
- Use `StateGraph` for main graph construction
- Properly compile graphs with `graph.compile()` and export as `app` variable
- Implement correct node functions with proper return types
- Use appropriate edge routing (conditional vs. simple edges)
- Design graphs based on your specific workflow requirements

**Tool Integration** (if your project uses tools):
- Use `@tool` decorator for tool definitions
- Include proper type hints for tool parameters and return values
- Implement error handling within tools
- Use `ToolNode` for tool execution in graphs
- Only implement tools that are relevant to your specific use case

**Graph Compilation**:
- Always ensure graphs compile successfully
- Export compiled app for external usage: `app = graph.compile()`
- Test basic invocation to verify functionality

## Error Handling and Logging

**Error Handling**:
- Use try-catch blocks for external API calls and tool operations
- Provide meaningful error messages that help with debugging
- Gracefully handle tool failures and network issues
- Implement fallback strategies where appropriate

**Logging**:
- Use Python's `logging` module instead of print statements
- Configure appropriate log levels (INFO, WARNING, ERROR)
- Include relevant context in log messages

## Testing Requirements

**Code Validation**:
- Ensure the application starts without import errors
- Verify graph compilation succeeds
- Test basic functionality with sample inputs appropriate to your use case
- Validate that any implemented tools work correctly
- Test edge cases and error conditions

**Manual Testing**:
- Test common user interaction patterns for your specific application
- Verify error handling with invalid inputs
- Ensure conversation flow works as expected (if applicable)
- Test any tools or external integrations thoroughly

## Environment and Configuration

**Environment Variables**:
- Use `.env` files for configuration (with `.env.example` template)
- Load environment variables with `python-dotenv`
- Never commit actual API keys or secrets

**Configuration Management**:
- Use environment variables for API keys and external service configuration
- Provide clear documentation for required environment variables
- Include sensible defaults where possible

## Documentation Standards

**Code Documentation**:
- Include docstrings for all functions and classes
- Document complex logic and non-obvious implementations
- Provide clear examples in docstrings for tools and main functions

**README Requirements**:
- Installation and setup instructions
- Usage examples and expected behavior
- Environment variable configuration
- Basic troubleshooting information

## Submission Checklist

Before considering any LangGraph implementation complete:

- [ ] **Ruff check passes**: `ruff check .` returns no errors
- [ ] **MyPy validation passes**: `mypy . --ignore-missing-imports` returns no type errors  
- [ ] **Graph compiles successfully**: No compilation errors in LangGraph
- [ ] **Application starts**: Can import and run without runtime errors
- [ ] **Core functionality works**: Main features operate as intended
- [ ] **Tools function correctly**: All implemented tools work as expected (if applicable)
- [ ] **Type hints included**: Comprehensive type annotations throughout
- [ ] **Error handling implemented**: Graceful handling of common failure scenarios
- [ ] **Requirements.txt complete**: All dependencies properly specified
- [ ] **Documentation updated**: README and code comments are clear and helpful

## Performance and Best Practices

**LangGraph Performance**:
- Use efficient state updates and avoid unnecessary state copying
- Implement proper checkpointing for memory management if needed
- Consider token limits and context management for longer conversations

**Python Best Practices**:
- Follow PEP 8 style guidelines
- Use appropriate data structures for the task
- Implement proper resource cleanup (context managers, etc.)
- Avoid common Python pitfalls (mutable default arguments, etc.)

Remember: The goal is to create production-quality LangGraph applications that are maintainable, type-safe, and follow established Python and LangGraph best practices.