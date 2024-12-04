My account plan demo app takes input in a number of categories about the current state of the account and suggests a strategy for state variables that are less than ideal. It's a very simple generative AI application, laying the groundwork for something more complicated later.

Built with Python and Gradio to leverage langchain libraries for llama 3.2 and openai gpt 4 functional models on my laptop.    I'll remove llama and add bedrock as I deploy to Lambda.

In its initial implementation it does not yet require the user to login and my intent is to acquire the necessary infrastructure for a test deployment.  After I deploy it to lambda in a test pilot, I'll add identity management and perhaps leave it running. 
