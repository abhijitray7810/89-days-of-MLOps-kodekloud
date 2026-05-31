The best experiment is **`pique-choc`** (revision `1f17277`) with:

* `n_estimators = 200`
* `accuracy = 0.94`
* `f1_score = 0.92` ← highest among all experiments

Current workspace is still on **`anile-newt`** (`n_estimators=500`, `f1_score=0.83`), so apply the winning experiment:

```bash
dvc exp apply 1f17277
```

(or)

```bash
dvc exp apply pique-choc
```

Then verify:

```bash
cat params.yaml
cat metrics.json
```

You should see `n_estimators: 200` and metrics corresponding to `accuracy: 0.94` and `f1_score: 0.92`.

Optionally confirm with:

```bash
git status
```

At that point, the workspace state (`params.yaml`, `metrics.json`, and `models/model.pkl`) will reflect the best-performing experiment, satisfying the lab requirement.
