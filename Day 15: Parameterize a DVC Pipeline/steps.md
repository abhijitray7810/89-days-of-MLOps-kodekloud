Your `dvc.yaml` is malformed at the end:

```yaml id="r8m4zk"
- models/model.pkl n_estimator: 100
```

The parameter definition was accidentally appended into `dvc.yaml`.
It should instead be in a separate `params.yaml` file, and the parameter name must exactly match `n_estimators`.

Fix it like this.

Correct `dvc.yaml`:

```bash id="v5q1pn"
cat > dvc.yaml <<'EOF'
stages:
  process_data:
    cmd: python src/data/process_data.py
    deps:
      - data/raw/transactions.csv
      - src/data/process_data.py
    outs:
      - data/processed/clean_transactions.csv

  split_data:
    cmd: python src/data/split_data.py
    deps:
      - data/processed/clean_transactions.csv
      - src/data/split_data.py
    outs:
      - data/processed/train.csv
      - data/processed/test.csv

  train:
    cmd: python src/models/train.py
    deps:
      - data/processed/train.csv
      - src/models/train.py
    params:
      - n_estimators
    outs:
      - models/model.pkl
EOF
```

Now create the correct `params.yaml`:

```bash id="f2x7tb"
cat > params.yaml <<'EOF'
n_estimators: 100
EOF
```

Run the pipeline:

```bash id="k9w3rm"
dvc repro
```

Verify status:

```bash id="d6p1qv"
dvc status
```

Now demonstrate parameter tracking by changing the parameter:

```bash id="u4m8zc"
cat > params.yaml <<'EOF'
n_estimators: 200
EOF
```

Re-run:

```bash id="y7t2kn"
dvc repro
```

Only the `train` stage should rerun.

Confirm the updated parameter is recorded:

```bash id="c3r9xl"
cat dvc.lock
```

Verify the model exists:

```bash id="p5v1mq"
ls -l models/model.pkl
```
