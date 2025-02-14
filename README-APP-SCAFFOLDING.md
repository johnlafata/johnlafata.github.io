# Application Templates

Below are a few applications that are examples to document the exercises associated with this workspace .  When applicable, architecture documents may be included for the applications using [diagramsAsCode](./tools/architecture/diagramsAsCode.md) to help visualize the architecture.

| App | Architecture | More Detail |
| :-- | :-- |  :-- |
| [Account Planning App](./README-APP-SCAFFOLDING.md#account-planning-application) | [application architecture](./doc/applications/account_planning/APP_ACCT_PLAN_ARCH.md) | [application detail](./doc/applications/account_planning/APP_ACCT_PLAN.md) |
| [RAG Document processing application](./README-APP-SCAFFOLDING.md#rag-document-processing-application) | [application architecture](./doc/applications/document_processing/APP_DOC_PROCESSING_ARCH.md) | [application detail](./doc/applications/document_processing/APP_DOC_PROCESSING.md) |
| [Product Conversational Knowledgebase app](./README-APP-SCAFFOLDING.md#product-conversational-knowledgebase-application) | [application architecture](./doc/applications/product_conversational_knowledge/APP_PROD_CONV_KNOWLEDGE_ARCH.md) | [application detail](./doc/applications/product_conversational_knowledge/APP_PROD_CONV_KNOWLEDGE.md) |


# Account Planning Application

A very simple chatbot app to recommend an account plan based on metrics associated with the account.  This is a simple python app using [python](./tools/code/language/python/pyenv.md), [gradio](./tools/code/language/python/gradio.md) for a UI and [langchain](./tools/code/ai/langchain.md) to call a choice of foundation models to make account strategy recommendations.

Here's a link to page where I am tracking the development progress for this application [My LLM based account planning application](./doc/applications/account_planning/APP_ACCT_PLAN.md)

# RAG Document processing Application

A chatbot that processes RAG documents and allows the user to request analysis of the document.  This is a simple python app using gradio for a UI and langchain to call a choice of foundation models to analyze the document.   Here's a link to page where I am tracking the development progress for this application [Document Processing Application](./doc/applications/document_processing/APP_DOC_PROCESSING.md)

# Product Conversational Knowledgebase Application

A chatbot functioning as a research assistant on product information.  This is a more complex python app using gradio for a UI and [langchain](./tools/code/ai/langchain.md) to call a choice of foundation models to provide product information.  I'm using llama-index and nVidia NEMO libraries to help with training and fine-tuning.   The application leverages tool calls to gather unstructured data and then leverages the llm to structure it into a [Pydantic](./tools/code/language/python/pydantic.md) object that we'll store in a vector database.

Here's a link to page where I am tracking the development progress for this application [My LLM based product conversational knowledge base application](./doc/applications/product_conversational_knowledge/APP_PROD_CONV_KNOWLEDGE.md)

