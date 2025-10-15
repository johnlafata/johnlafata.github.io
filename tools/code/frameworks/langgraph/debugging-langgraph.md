DEBUGGING LANGGRAPH:

Debugging LangGraph applications effectively involves a combination of tools and techniques to understand the flow and state of your agentic systems.
1. LangGraph Studio:
Visualization and Interaction: LangGraph Studio provides a visual interface for interacting with and debugging your LangGraph agents. It allows you to see the execution flow between nodes, inspect the state at each step, and identify where errors occur.
Time Travel Debugging: Studio offers the ability to "time travel" through your agent's execution, rolling back to specific points in time to examine the state and make modifications.
Local Execution and Editing: You can run and debug your agents locally within Studio, and even edit prompts and configurations directly in the interface.
2. Streaming and Checkpointing:
Stream Mode: When running your LangGraph, use stream_mode="debug" to get a verbose output stream that includes inputs, outputs, tool calls, metadata, and state information for each step. This provides a live view of your graph's execution.
Checkpointers: Utilize checkpointers (e.g., MemorySaver for in-memory or persistent stores like Postgres) to save snapshots of your graph's state at various points. These snapshots allow you to "look back in time" and analyze the state at specific steps, helping to pinpoint issues.
3. LangSmith Tracing:
Comprehensive Tracing: LangSmith offers robust tracing capabilities for your LLM applications, including LangGraph. It logs all events in your chain, providing a detailed visualization of the execution flow, LLM calls, and intermediate outputs.
Integration with Studio: LangSmith integrates with LangGraph Studio, allowing you to pull down production traces and debug them locally, offering a powerful way to understand and resolve issues encountered in deployed agents.
4. Code-Level Debugging:
Python Debugger: For deeper code-level issues within your LangGraph nodes, use standard Python debugging tools like the VS Code Python Debugger or PyCharm's debugger to set breakpoints, step through code, and inspect variables.
Logging and Print Statements: Strategically placed logging or print statements within your node functions can provide valuable insights into the data and logic at specific points during execution.
5. Isolating Nodes for Testing:
Interrupt After: When testing or debugging a specific part of your graph, use the interrupt_after parameter when compiling the graph to stop execution after a desired node. This allows you to focus on a particular section without running the entire graph.
By combining these methods, you can gain a comprehensive understanding of your LangGraph application's behavior and efficiently identify and resolve any issues.


## Reference:
https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/add-human-in-the-loop/?h=local+studio#debug-with-interrupts

[1] https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/
[2] https://langchain-ai.github.io/langgraph/how-tos/local-studio/
[3] https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/
[4] https://langchain-ai.github.io/langgraph/concepts/langgraph_checkpoints/
[5] https://langchain-ai.github.io/langgraph/how-tos/checkpoints/
[6] https://langsmith.langchain.com/docs/getting-started/introduction
[7] https://langsmith.langchain.com/docs/guides/tracing
[8] https://langsmith.langchain.com/docs/guides/langgraph-integration
[9] https://code.visualstudio.com/docs/python/debugging
[10] https://www.jetbrains.com/help/pycharm/debugging-code.html