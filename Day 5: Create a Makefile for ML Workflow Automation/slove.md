# Corrected Makefile for /root/code/fraud-detection/

```Makefile
.PHONY: setup data train test clean all

setup:
	python3 -m venv mlops-venv
	./mlops-venv/bin/pip install --upgrade pip
	./mlops-venv/bin/pip install -r requirements.txt

data:
	python src/data/process_data.py

train:
	python src/models/train.py

test:
	pytest tests/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf models/*

all: setup data train test
```

## Steps to Apply

```bash
cd /root/code/fraud-detection/

# Edit the Makefile
vi Makefile

# Run the pipeline
make all
```

## Important Notes

* Every recipe line must start with a real TAB character.
* Do not replace TABs with spaces.
* `all` executes targets in this order:

  1. setup
  2. data
  3. train
  4. test
