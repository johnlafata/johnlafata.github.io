I am going to start with a basic chatbot which I'm going to use as a research assistant.

What does it take to build an inference application such as a chatbot?
I basically want to use the natural language processing of the chat bot collect  research and build a training dataset.

* I need to choose a foundation model
* I need to do some prompt engineering to help guide the model to give answers I think are appropriate.
* I need to train the model on a dataset.
* I also want to integrate the model to some research resources to help get more information that the model is trained for.
* I also want to include Vector database to store the research and to later guide the response following a Retreival Augment Generation architecture.

I'm going to start with a python application langchain that uses Openai as a foundation model.  Using Openai is pretty simple, you need to register with open ai to get an api key, then you can use the Openai python library to interact with the api.   

I put a nominal charge on my Openai account to get started and I'm going to be careful to monitor my usage so I don't overrun the allocation I committed, but I'm also interested in using oLLama based models on my laptop to prove out functionality without incurring costs.

Using langchain, I'm not limited to Openai or ollama, I can use any foundation model I want.  I'm going to start with Openai, but I'm also going to look at using the llama-index models from meta.  I'm going to use the llama-index to help me collect research and training data.  I'm going to use the Arxiv and Wikipedia retrievers to help me with this.  I'm also going to use the nvidia NIM curator to help me with training data.

At some point, I'm may want to deploy this to the cloud, so I'm going investigate how to deploy that on AWS Bedrock, which is a new service that allows you to deploy multimodal vision and lightweight models.  I'm also going to look at deploying on AWS Lambda.

# Initial Architecture

Here's an initial high level architecture of the chatbot application I'm going to build.

* I will use both OpenAI and Llama3.2/3B as foundation model
* I need to do some prompt engineering to help guide the model to give answers I think are appropriate.
* I need to train the model on a dataset.
* I also want to integrate the model to some research resources to help get more information that the model is trained for.
* I also want to include Vector database to store the research and to later guide the response following a Retrieval Augment Generation architecture.

![KnowledgeBase application](./images/knowledgeBase-application.png)

# tools integration
- Spring REST
- FastAPI
- pydantic code generator - convert openai to pydantic model
- Specrawler - Generating OpenAPI Specifications from API Documentation Using Large Language Models
    https://arxiv.org/abs/2402.11625

# training
llama3.2 with pydantic models
    Use case: generate structured output from unstructured text
    Use case: generate sample training data
    https://docs.llamaindex.ai/en/stable/examples/output_parsing/function_program/
    https://docs.pydantic.dev/latest/integrations/datamodel_code_generator/#example

    fine-tuning on dataset input
    https://docs.llamaindex.ai/en/stable/examples/finetuning/openai_fine_tuning_functions/ 

    more fine-tuning
    https://developer.nvidia.com/blog/fine-tune-and-align-llms-easily-with-nvidia-nemo-customizer/

    https://github.com/openai/openai-cookbook/blob/main/examples/data/toy_chat_fine_tuning.jsonl

# generating training data
Run program to get structured output.
    Use case: Embed to local vector store -  search for "Load documents, build the VectorStoreIndex" in following reference)
    https://docs.llamaindex.ai/en/stable/examples/output_parsing/nvidia_output_parsing/ 


Get data from external sources via llama-index packages
    Arxiv: 
    https://python.langchain.com/docs/integrations/retrievers/Arxiv/
    https://arxiv.org/search/?query=foot&searchtype=all&abstracts=show&order=&size=50
    Wikipedia: 
    https://llamahub.ai/l/readers/llama-index-readers-wikipedia
    Web Page reader:
    https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/

    load and search tool (tool that wraps any data loader, and is able to load data on-demand.)
    https://docs.llamaindex.ai/en/stable/api_reference/tools/load_and_search/

    google:
    https://llamahub.ai/l/tools/llama-index-tools-google?from=tools
    https://github.com/run-llama/llama_index/tree/main/llama-index-integrations/tools/llama-index-tools-google 

more fine tuning references:
    https://www.llama.com/docs/how-to-guides/fine-tuning/
    https://www.datacamp.com/tutorial/fine-tuning-llama-3-2
    https://pytorch.org/torchtune/0.3/tutorials/chat.html
    fine-tuning mistral... is this an online fine-tuning vs on desktop?
    https://www.restack.io/p/fine-tuning-answer-jsonl-example-cat-ai


insert data into vector store
Milvus (in docker on mac)
    https://medium.com/@ankushrastogi04/setting-up-milvus-vector-database-on-a-local-mac-4802def8d4dc#:~:text=This%20guide%20will%20walk%20you,similarity%20searches%20and%20AI%20applications.
pinecone (SaaS)
    https://docs.pinecone.io/guides/get-started/quickstart
    https://docs.llamaindex.ai/en/stable/examples/output_parsing/nvidia_output_parsing/
    https://docs.pinecone.io/guides/get-started/build-a-rag-chatbot
Postgres vector
    https://github.com/pgvector/pgvector
    https://formulae.brew.sh/formula/pgvector
    https://www.postgresql.org/docs/14/pgtrgm.html
On Cloud (mazon DynamoDB)
    https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html


Embed content from pdf files
    Smart PDF Loader

Llama Hub
    https://llamahub.ai › llama-index-readers-smart-pdf-loader

nVidia NIM curator
    filtering the dataset
    https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/qualityfiltering.html
    https://developer.nvidia.com/blog/curating-custom-datasets-for-llm-parameter-efficient-fine-tuning-with-nvidia-nemo-curator/
    https://developer.nvidia.com/blog/curating-trillion-token-datasets-introducing-nemo-data-curator/
    https://developer.nvidia.com/blog/scale-and-curate-high-quality-datasets-for-llm-training-with-nemo-curator/

# running locally (in Docker)?
https://github.com/closedai-project/closedai
https://chenhunghan.github.io/ialacol/
https://github.com/mudler/LocalAI
https://github.com/zylon-ai/private-gpt

# hosting on cloud
- S3 for training data storage
- Lambda app
    - python langchain app
    - running gradio app on AWS
        https://abidlabs.medium.com/quickly-deploying-gradio-on-aws-242af2374784
- Bedrock

https://aws.amazon.com/blogs/machine-learning/create-a-multimodal-chatbot-tailored-to-your-unique-dataset-with-amazon-bedrock-fms/

https://aws.amazon.com/blogs/aws/introducing-llama-3-2-models-from-meta-in-amazon-bedrock-a-new-generation-of-multimodal-vision-and-lightweight-models/

https://aws.amazon.com/blogs/machine-learning/build-generative-ai-chatbots-using-prompt-engineering-with-amazon-redshift-and-amazon-bedrock/

https://aws.amazon.com/blogs/machine-learning/improve-llm-application-robustness-with-amazon-bedrock-guardrails-and-amazon-bedrock-agents/

https://docs.aws.amazon.com/decision-guides/latest/bedrock-or-sagemaker/bedrock-or-sagemaker.html

https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html

https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html

https://aws.amazon.com/blogs/machine-learning/fine-tune-meta-llama-3-2-text-generation-models-for-generative-ai-inference-using-amazon-sagemaker-jumpstart/

- - youtube video
- - - [Fine-Tuning your Foundation Model in Amazon Bedrock | Amazon Web Services](https://www.youtube.com/watch?v=Sh1XBtf8ISg)
- SageMaker?

Future topics

# Security / Compliance
- Spring Security
    identity management
- nvidia Guardrails
    https://github.com/NVIDIA/NeMo-Guardrails

# Observability
- Arize Pheonix
https://colab.research.google.com/drive/1xmq4tbnlH9e96rwFrJ3hS3wRsnB4LoSs#scrollTo=ss0Es3X32Vu1
https://adasci.org/a-hands-on-guide-to-arize-phoenix-for-llm-observability/ 
- Llama trace
