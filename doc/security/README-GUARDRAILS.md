### Guardrails for GEN AI Apps
Safeguard sensitive information and critical systems, ensuring data integrity and confidentiality. 
Prevent malicious activities such as injection attacks or unauthorized access attempts by validating and filtering user input before processing it.

## nVidia NEMO Guardrails
NeMo Guardrails are programmable guardrails that can be easily added to large language model (LLM)-based conversational applications. These guardrails provide a way to control the output of the language model, guiding and safeguarding conversations by defining specific behaviors, such as restricting discussions on certain topics, directing dialog paths, enforcing language styles, extracting structured data, and more.

To code NEMO Guardrails, developers can easily add programmable guardrails between the application code and the large language model (LLM). This allows for fine-grained control over the behavior of the LLM-based applications. By defining rails, developers can guide and safeguard conversations, control the topics the LLM engages with, connect the LLM to other services securely, and steer the LLM to follow predefined conversational paths. This enables the design of interactions following conversation design best practices and the enforcement of standard operating procedures.

### Installation
https://docs.nvidia.com/nemo/guardrails/introduction.html#installation

### Example Guardrail Configuration file

```
# config.yml
models:
  - type: main
    engine: openai
    model: gpt-3.5-turbo-instruct

rails:
  # Input rails are invoked when new input from the user is received.
  input:
    flows:
      - check jailbreak
      - mask sensitive data on input

  # Output rails are triggered after a bot message has been generated.
  output:
    flows:
      - self check facts
      - self check hallucination
      - activefence moderation
      - gotitai rag truthcheck

  config:
    # Configure the types of entities that should be masked on user input.
    sensitive_data_detection:
      input:
        entities:
          - PERSON
          - EMAIL_ADDRESS
```