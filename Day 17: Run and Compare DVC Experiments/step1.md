The snippet shows the `train` stage is parameterized by `n_estimators`, so the equivalent DVC experiment workflow would be:

```bash
cd /root/code/fraud-detection

# Run three experiments with different values
dvc exp run -S n_estimators=50
dvc exp run -S n_estimators=200
dvc exp run -S n_estimators=500

# Compare results
dvc exp show
```

The output of `dvc exp show` will contain each experiment's metrics (including `f1_score`) and parameter values. Select the experiment with the highest `f1_score`, then apply it to the workspace:

```bash
dvc exp apply <experiment-name-or-rev>
```

Finally, make the workspace reflect the promoted experiment's tracked state:

```bash
git status   # verify changes (params.yaml, metrics.json, model artifacts, etc.)
```

I still can't determine which experiment actually won because I don't have access to the repository or the `dvc exp show` output. If you paste the result of:

```bash
dvc exp show
```

I can identify the best experiment and tell you exactly which one to apply.
