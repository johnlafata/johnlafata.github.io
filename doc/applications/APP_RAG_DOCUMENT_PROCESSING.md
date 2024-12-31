This Retrieval Augmented Generation App allows the user to load a document into an in memory vector database and then ask OpenAI to use it in a conversation. The user can ask questions about the document and the app will return the answer. The user can also ask the app to generate a summary of the document.

The following is a quick little example of my use of the app to load a very detailed copy of a resume and then compare it to a job description.   I then prompt it to extract and enhance specific experience from the resume.   I also have used it to answer questions about the experience and to generate a cover letter highlighting relevant experience.

For how I run it on my macbook pro, in the future I look to add more features and make it more user friendly.  I also plan to add more examples of how I use it.

1. require a login
2. make it multi-tenanted
3. update it to use other functional models
4. run it on the cloud
5. update it to use other vector database products

Here's a screenshot of the initial UI:

![Initialized application](../../images/app-rag-document-processing/1-init.png)

Here's a screenshot of the application selecting a document to load:

![Selecting a document](../../images/app-rag-document-processing/2-selectFile.png)

This screenshot shows the status as it loads the document;

![Loading the document](../../images/app-rag-document-processing/3-ingestContext.png)

In this screenshot, I add the job description and instructions in a user prompt:

![Adding the job description](../../images/app-rag-document-processing/4-addPrompt.png)

Finally, this screenshot shows the response to the request:

![Response to the request](../../images/app-rag-document-processing/5-completion1.png)


