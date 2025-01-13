# pydantic datamodel code generator
## reference
https://docs.pydantic.dev/latest/integrations/datamodel_code_generator/

https://koxudaxi.github.io/datamodel-code-generator/

### setup
do this within in a python virtual environment
#### create a python virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
#### install the datamodel code generator
```bash
pip install datamodel-code-generator
```

### or install it with the http extra model to read openqapi spec hosted by spring boot using spring REST docs
```bash
pip install 'datamodel-code-generator[http]'
```

we have an openapi spec hosted by spring boot using spring REST docs at
[locahost:8080/v3/api-docs](http://localhost:8080/v3/api-docs)
```bash

### usage
```bash
datamodel-codegen --url http://localhost:8080/v3/api-docs --output model.py
```
### results
```bash
The input file type was determined to be: openapi
This can be specified explicitly with the `--input-file-type` option.
% 
```

### now that I have a model, I want to call the rest api via python request mode
#### reference:
https://docs.python-requests.org/en/latest/user/quickstart/

```python
```