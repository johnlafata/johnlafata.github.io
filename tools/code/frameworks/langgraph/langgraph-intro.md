# langgraph

https://langchain-ai.github.io/langgraph/

## Running LangGraph on a MacBook

To run LangGraph on a local MacBook, you need to install the LangGraph CLI, set up a LangGraph application with a "langgraph.json" configuration file, and then use the langgraph dev command to start a local server, which can be accessed through the LangGraph Studio interface in your browser; essentially requiring Docker to be installed on your machine to run the local server properly.   

Key steps:   
• Install necessary tools:   
	• Install Docker on your MacBook. 
	• Install the LangGraph CLI using `pip install langgraph`.   

• Create a LangGraph application:   
	• Set up a project directory with your LangGraph logic defined in Python code.   
	• Create a "langgraph.json" file to configure your graph structure and dependencies. ]  

• Start the local server:   
	• Navigate to your project directory in the terminal.  
	• Run the command `langgraph dev` to start the LangGraph API server in development mode.   

• Access LangGraph Studio:   
	• Once the server is running, open a web browser and go to http://127.0.0.1:2024 to access the LangGraph Studio interface.   
	• You should see your defined LangGraph in the Studio UI where you can interact with it and run simulations. 

Important points to remember:   
• LangSmith integration: To fully utilize LangGraph Studio, you might need to authenticate with a LangSmith account.   
• Persistent storage: For production use, consider using the langgraph up command instead of langgraph dev to run the server with a persistent storage backend.   
• Debugging and development: The local development environment allows you to easily test changes to your LangGraph application and see immediate updates in the Studio.   

##  Reference:

[1] https://github.com/langchain-ai/langgraph-studio
[2] https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/
[3] https://github.com/langchain-ai/langgraph-studio/blob/main/README.md
[4] https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/
[5] https://www.youtube.com/watch?v=YXFqyRKu9TA
[6] https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/
[7] https://www.youtube.com/watch?v=o9CT5ohRHzY
[8] https://langchain-ai.github.io/langgraph/how-tos/local-studio/
[9] https://langchain-ai.github.io/langgraph/cloud/how-tos/test_local_deployment/
[10] https://langchain-ai.github.io/langgraphjs/tutorials/langgraph-platform/local-server/
