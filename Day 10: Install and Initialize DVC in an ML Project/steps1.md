Run these commands in the terminal:

```bash
cd /root/code/fraud-detection

dvc init

git add .dvc .dvcignore

git commit -m "Initialize DVC"
```

You can verify it worked with:

```bash
git log --oneline -1
ls -a
```

You should now see:

* `.dvc/`
* `.dvcignore`

and the latest Git commit message:
`Initialize DVC`
