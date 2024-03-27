from langchain.tools import tool

@tool("Execute CLI command")
def execute_command(command):
    """Execute a command in the command line."""
    print(f"Executing command: {command}")
    return os.system(command)