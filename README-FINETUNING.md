**Product Conversational Knowledgebase app**

I developed this code to produce and ingest datasets into a vector database for a chatbot functioning as a research assistant on product information.  This is a more complex python app using gradio for a UI and [langchain](./tools/code/ai/langchain.md) to call a choice of foundation models to provide product information.  I'm using llama-index and nVidia NEMO libraries to help with training and fine-tuning.   The application leverages tool calls to gather unstructured data and then leverages the llm to structure it into a [Pydantic](./tools/code/language/python/pydantic.md) object that we'll store in a vector database.


### Tools used
python, langchain, llama-index (Arxiv, Wikipedia), nvidia NEMO Curator, Pydantic to format unstructured data into structured dataset
