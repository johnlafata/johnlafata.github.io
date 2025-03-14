My account plan demo app takes input in a number of categories about the current state of the account and suggests a strategy for state variables that are less than ideal. It's a very simple generative AI application, laying the groundwork for something more complicated later.

Built with Python and Gradio to leverage langchain libraries for Ollama's llama 3.2, OpenAI GPT 4.0, Anthropic Claude, Anthropic Haiku and Groq using Llama3.3 foundation models to run on my laptop and on AWS fargate.

Currently, this is a pilot that runs on my macbook pro and AWS Fargate, keep posted for th following updates:

1. require a login with AWS Cognito on AWS deployments
2. make the application multi-tenanted to allow multiple users to use it simultaneously
4. add additional foundation models to the application

Here's a few screenshots showing how the account planning application works:

1. Specify the current state of the account and update the prompt with what ever you think is useful

![Account Planning App](./runtime_images/1-specifyCurrentState.png)

2. Specify Chat parameters to influence the token processing

![Account Planning App](./runtime_images/2-specifyChatbotParameters.png)

3. submit your request

![Account Planning App](./runtime_images/3-submitRequest.png)

4. get your results

![Account Planning App](./runtime_images/4-getCompletionResponse.png)

