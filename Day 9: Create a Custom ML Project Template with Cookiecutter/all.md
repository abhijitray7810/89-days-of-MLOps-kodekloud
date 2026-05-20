Update the Cookiecutter template so it has this exact structure:

```text
/root/code/mlops-template/
├── cookiecutter.json
└── {{cookiecutter.project_name}}/
    ├── README.md
    ├── requirements.txt
    ├── data/
    ├── models/
    ├── src/
    └── tests/
```

Use these exact file contents.

`cookiecutter.json`

```json
{
  "project_name": "my-ml-project",
  "author": "xFusionCorp",
  "python_version": "3.11",
  "ml_framework": [
    "sklearn",
    "pytorch",
    "tensorflow"
  ]
}
```

`{{cookiecutter.project_name}}/README.md`

```md
# {{ cookiecutter.project_name }}

Author: {{ cookiecutter.author }}

This machine learning project was generated using the xFusionCorp MLOps Cookiecutter template.
```

`{{cookiecutter.project_name}}/requirements.txt`

```txt
{% if cookiecutter.ml_framework == "sklearn" %}
scikit-learn
{% elif cookiecutter.ml_framework == "pytorch" %}
torch
{% elif cookiecutter.ml_framework == "tensorflow" %}
tensorflow
{% endif %}
```

Create the required directories:

```bash
mkdir -p "{{cookiecutter.project_name}}"/{data,models,src,tests}
```

Then generate the project:

```bash
cookiecutter /root/code/mlops-template/ -o /root/code/ --no-input project_name=churn-model ml_framework=sklearn
```

Verify:

```bash
cat /root/code/churn-model/requirements.txt
cat /root/code/churn-model/README.md
```

Expected results:

`requirements.txt`

```txt
scikit-learn
```

`README.md` should mention:

```txt
xFusionCorp
```
