```bash
cd /root/code/fraud-detection
```

Then run the commands:

```bash
git rm --cached data/raw/transactions.csv
dvc add data/raw/transactions.csv
git add data/raw/transactions.csv.dvc data/raw/.gitignore
git commit -m "Track transactions dataset with DVC"
```

Also note — in your first attempt you had a typo: `trabsactions.csv` instead of `transactions.csv`. The commands above have the correct spelling.
