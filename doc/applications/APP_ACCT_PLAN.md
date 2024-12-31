My account plan demo app takes input in a number of categories about the current state of the account and suggests a strategy for state variables that are less than ideal. It's a very simple generative AI application, laying the groundwork for something more complicated later.

Built with Python and Gradio to leverage langchain libraries for llama 3.2 and openai gpt 4 functional models on my laptop.    

Currently, this is a pilot that runs on my macbook pro, In the future I may add the following improvements:

1. require a login
2. make the application multi-tenanted to allow multiple users to use it
3. run it on the cloud
4. add additional foundation models to the application

Here's a few screenshots showing how the account planning application works:

1. Specify the current state of the account and update the prompt with what ever you think is useful

![Account Planning App](../../images/app-inference-account-planning/1-specifyCurrentState.png)

2. Specify Chat parameters to influence the token processing

![Account Planning App](../../images/app-inference-account-planning/2-specifyChatbotParameters.png)

3. submit your request

![Account Planning App](../../images/app-inference-account-planning/3-submitRequest.png)

4. get your results

![Account Planning App](../../images/app-inference-account-planning/4-getCompletionResponse.png)

### llama32 recommended account plan

The response is longer than fits in the screenshot, so I extracted it here to show the full response.
```
Based on the provided account status, I recommend a multi-faceted strategy to improve the relationship status. Since the relationship status is BAD and the budget status is also limited, we'll focus on demonstrating value and building momentum.

Strategy: "Developer Champions"

Identify Developer Champions: Reach out to your existing contacts for developers who are using our products. These individuals can serve as advocates and help promote our solutions within their teams.
Executive Org Chart Engagement: Utilize the executive org chart to identify key decision-makers and influencers. Schedule meetings with these executives to discuss how our products can address specific business challenges or opportunities.

Quick ROI Demonstration: Prepare a concise, data-driven presentation showcasing the potential return on investment (ROI) for a specific transaction. This will help demonstrate the value of our solutions and potentially alleviate budget concerns.
Value-Added Content: Develop targeted content (e.g., blog posts, whitepapers, case studies) highlighting the benefits of our products in addressing common business challenges. Share this content with the developer champions and executive decision-makers to build credibility and trust.

Regular Progress Updates: Schedule regular check-ins with the developer champions and executive decision-makers to provide updates on your progress, address any concerns, and demonstrate continued value.

Additional Recommendations

Consider offering a limited-time promotion or discount for new transactions to incentivize adoption.
Leverage social proof by sharing success stories from similar organizations that have implemented our solutions.
Be prepared to discuss how our products can help the customer achieve specific business objectives, such as cost savings or revenue growth.

By implementing this strategy, you should be able to improve the account status and demonstrate value to the customer.
```


### openai gpt 4 recommended account plan

Switch the foundation model and submit to another model to see what it recommends.  

```
Based on the account status details provided, here are the strategies to improve each aspect of your account that is not in good status:

Relationship Status: BAD
Strategy: Since the relationship status is bad but you have contacts with developers and access to an executive org chart, use these resources to identify key stakeholders and decision-makers. Plan a dramatic engagement strategy by organizing a high-impact meeting or workshop that includes demonstrations of how your products can solve specific problems faced by the company. Tailor this session to the interests and pain points of the stakeholders, leveraging the developers' positive experiences with your products as case studies.

Product Adoption Status: FAIR
Strategy: To improve product adoption, focus on educating and training the developers further on the full capabilities of your products. Offer webinars, detailed documentation, and hands-on workshops to help them utilize your products more effectively. Additionally, gather feedback from these developers to understand any barriers they are facing and address these issues promptly.

Customer Budget Status: BAD
Strategy: Since the budget is limited, focus on demonstrating a quick Return on Investment (ROI). Prepare a detailed analysis showing the cost savings and efficiency gains from using your products. Highlight case studies or data points from the developers currently using your products to strengthen your case. Propose a pilot project or phased implementation that requires minimal upfront investment but can quickly demonstrate value.

Customer Business Metrics Status: FAIR
Strategy: Work closely with a champion within the company to collect and analyze business metrics before and after further adoption of your products. Document these metrics to demonstrate the tangible benefits your products bring to the organization. Use this data to build a compelling business case for wider adoption, focusing on measurable improvements in productivity, cost savings, or other relevant business outcomes.

By implementing these strategies, you can work towards improving the overall status of your account, turning challenges into opportunities for deeper engagement and collaboration.
```