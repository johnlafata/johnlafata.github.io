# My Studio
This repo is where I am sharing my thoughts and experience as a cloud architect.   I'm gradually going to release projects, experiments, and learnings here.  

Some sample topics may include containerizing a legacy application, deploying an inference application, migrating code to a cloud ready architecture, or automating infrastructure provisioning.   

---

## Baseline Development Infrastructure
### Repo Security

This link presents my evaluation of github hooks for [secret scanning](./doc/security/REPO-SECURITY-README.md). I'm going to use this as a starting point for protecting myself from accidentally deploying secrets or tokens to my repos.

### Next, integrate with a secrets manager to make things work

While working on my laptop, I currently am using environment variables stored on my local desktop to specify secrets, in time I will incorporate a secrets manager.  

### Identity management
When I deploy to the cloud I'd like to ensure that I have a good identity management strategy.  

I'm going to start with AWS Cognito, but I'm also going to look at Okta and Auth0.  I'm going to use the AWS Cognito SDK to help me with this.

## DevSecOps

Here are some notes on the application deployment tests I am working on. [DevOps](./doc/devops/INTRO.md)


## Demo apps

Below are a few applications that I'm working on to document my learning and experience.  When applicable, I'll add architecture documents for the applications using [diagramsAsCode](./tools/architecture/diagramsAsCode.md) to help me visualize the architecture.

**Account Planning App**

A very simple chatbot app to recommend an account plan based on metrics associated with the account.  This is a simple python app using [python](./tools/code/language/python/pyenv.md), [gradio](./tools/code/language/python/gradio.md) for a UI and [langchain](./tools/code/ai/langchain.md) to call a choice of foundation models to make account strategy recommendations.

Here's a link to page where I am tracking the development progress for this application [My LLM based account planning application](./doc/applications/APP_ACCT_PLAN.md)

**Product Conversational Knowledgebase app**

A chatbot functioning as a research assistant on product information.  This is a more complex python app using gradio for a UI and [langchain](./tools/code/ai/langchain.md) to call a choice of foundation models to provide product information.  I'm using llama-index and nVidia NEMO libraries to help with training and fine-tuning.   The application leverages tool calls to gather unstructured data and then leverages the llm to structure it into a [Pydantic](./tools/code/language/python/pydantic.md) object that we'll store in a vector database.

Here's a link to page where I am tracking the development progress for this application [My LLM based product conversational knowledge base application](./doc/applications/APP_PROD_CONV_KNOWLEDGE.md)


