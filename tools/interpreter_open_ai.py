from langchain.tools import tool
from interpreter import interpreter

@tool("Interpret code with OpenAI")
def interpret_code_with_openai(code):
    """
    Interpret code using the OpenAI Codex model.

    Args:
        code (str): The code to be interpreted.

    Returns:
        str: The interpretation of the code.
    """
    
    interpreter.offline = True # Disables online features like Open Procedures
    interpreter.llm.model = "openai/x" # Tells OI to send messages in OpenAI's format
    interpreter.llm.api_key = "fake_key" # LiteLLM, which we use to talk to LM Studio, requires this
    interpreter.llm.api_base = "http://localhost:1234/v1" # Point this at any OpenAI compatible server
    
    return interpreter.chat(code)