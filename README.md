# mcp-server-count-letters MCP server

A MCP letter counter

## Components

### Resources

The server implements a simple note storage system with:
- Custom mcp:// URI scheme for r's in strawberry and raspberry

### Tools

The server implements two tools:
- count_letter: counts the occurrences of a specified letter
  - Takes "word" and "letter" as required string arguments
  - Returns an integer of the occurences

This MCP server is the working code sample of the blog post [Building a MCP Server so LLMs Can Count Letters](https://www.higherpass.com/2025/04/29/building-a-mcp-server-so-llms-can-count-letters/)
