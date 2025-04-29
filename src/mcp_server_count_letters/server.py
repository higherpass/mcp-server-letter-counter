from fastmcp import FastMCP
from typing import Dict, Any

# Initialize the MCP server
mcp = FastMCP("letter-counter")

# Define the letter counting tool
@mcp.tool()
def count_letter(word: str, letter: str) -> int:
    count = word.lower().count(letter.lower())
    return count

# Define resources for counting 'r's in strawberry and raspberry
@mcp.resource(uri="mcp://strawberry")
def r_in_strawberry() -> int:
    count = count_letter("strawberry", "r")
    return count

@mcp.resource(uri="mcp://raspberry")
def r_in_raspberry() -> int:
    count = count_letter("raspberry", "r")
    return count

# Run the server
if __name__ == "__main__":
    mcp.run()
