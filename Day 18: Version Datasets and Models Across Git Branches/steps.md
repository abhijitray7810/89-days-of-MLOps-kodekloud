To complete the task, run the following commands from the repository root:

```bash
cd /root/code/fraud-detection
```

### 1. Tag the current state on `main` as `v1.0`

```bash
git tag v1.0
```

### 2. Create and switch to the `v2-improved` branch

```bash
git checkout -b v2-improved
```

### 3. Replace the tracked dataset with the improved version

```bash
cp data/raw/transactions_v2.csv data/raw/transactions.csv
```

### 4. Re-track the dataset with DVC

If `transactions.csv` is already DVC-tracked, updating the file contents is enough. Reproduce the pipeline:

```bash
dvc repro
```

### 5. Commit the updated dataset and pipeline outputs

```bash
git add data/raw/transactions.csv.dvc dvc.lock metrics.json models data/raw/transactions.csv
git commit -m "Use improved dataset and retrain model"
```

(If Git reports different files as modified, add those instead.)

### 6. Switch back to `main`

```bash
git checkout main
```

### 7. Restore the v1 dataset tracked on `main`

```bash
dvc checkout
```

### 8. Verify the restored dataset matches the `v1.0` tag

Compare the hash recorded in the tag with the current one:

```bash
git show v1.0:data/raw/transactions.csv.dvc
cat data/raw/transactions.csv.dvc
```

The DVC hash (`md5`) in the current `.dvc` file should match the one stored in the `v1.0` tag.

You can also confirm branch-specific tracked state:

```bash
dvc status
git branch
```

After these steps:

* `main` is tagged as `v1.0`
* `v2-improved` contains the newer dataset and retrained outputs
* Returning to `main` and running `dvc checkout` restores the original dataset version recorded by the `v1.0` state.
