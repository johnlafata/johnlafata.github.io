# langgraph

## Intro 
LangGraph is a library designed for building stateful, multi-actor applications using Large Language Models (LLMs). It enables the creation of agent and multi-agent workflows, inspired by Pregel and Apache Beam. LangGraph offers fine-grained control over the flow and state of agent applications, with features like memory persistence for conversation history and human-in-the-loop capabilities. It standardizes components to allow focus on agent behavior rather than infrastructure. LangGraph Platform provides tooling for developing, deploying, debugging, and monitoring applications, seamlessly integrating with LangChain and LangSmith.

## Reference
https://blog.blockmagnates.com/langchain-vs-langgraph-a-comprehensive-comparison-of-language-model-frameworks-ec8a88785c6d#:~:text=1.,Integration%20with%20External%20Data%20Sources

https://github.com/langchain-ai/langgraph#:~:text=LangGraph%20is%20a%20library%20for,and%20monitoring%20of%20your%20applications.


## langgraph with DAG's apache airflow or TensorFlow Extended
LangGraph complements Apache Airflow or TensorFlow Extended by offering a visual and graph-based approach to workflow orchestration, which can be particularly beneficial for users who prefer a more intuitive representation of task dependencies and flow control. This emphasis on declarative workflows and graphical interfaces provides an alternative to the code-based structures of Apache Airflow or TensorFlow Extended, allowing for easier visualization and management of complex workflows in LLM-based applications.

While langgraph does involve a graph-based architecture where nodes represent individual actors and edges define relationships and flow of data, LangGraph introduces additional features and capabilities beyond what is typically found in a traditional DAG framework.

## reference
https://ai.gopubby.com/langgraphs-cutting-edge-approach-to-automated-assistance-8c7d9bcda491#:~:text=Examples%20of%20DAG%20frameworks%20include%20Apache%20Airflow,features%20and%20capabilities%20beyond%20what%20is%20typically

