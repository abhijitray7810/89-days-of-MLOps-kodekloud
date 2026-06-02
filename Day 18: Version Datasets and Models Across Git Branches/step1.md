I can't provide a successful completion result for those Git/DVC tasks because the repository isn't available in the environment I can access.

A quick check shows that `/root/code/fraud-detection` does not exist here, so I can't run commands such as:

```bash
git tag v1.0
git checkout -b v2-improved
dvc add data/raw/transactions.csv
dvc repro
git commit ...
git checkout main
dvc checkout
```

Without access to the actual repository and DVC metadata, I also can't verify dataset hashes or confirm that `dvc checkout` restores the version associated with the `v1.0` tag.

If the repository is available in another workspace, provide the correct path or make the files accessible, and I can carry out and verify the requested operations.
