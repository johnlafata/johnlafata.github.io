# Model Context Protocol (MCP)

### LangChain and Model Context Protocol (MCP)

LangChain is a framework for developing applications powered by language models. As of now, LangChain does not natively support the Model Context Protocol (MCP). However, you can integrate MCP with LangChain by creating custom connectors and interfaces that adhere to the MCP specification.

To integrate MCP with LangChain, follow these steps:

1. **Create an MCP Server**: Develop a connector that communicates with the AI models using MCP. Refer to the "Building an MCP Connector" section above for guidance.

2. **Integrate the MCP Server into LangChain**: Use an MCP Client within your LangChain application to interact with the AI models.


# Example implementation 

Here is an example repo demonstrating how to incorporate MCP into a langgraph application:

[https://github.com/johnlafata/mcp-langgraph](https://github.com/johnlafata/mcp-langgraph)