Your `.dvc/config` is missing the required credentials for the S3 remote.

From `/root/code/fraud-detection`, run:

```bash id="q7v2mk"
dvc remote modify s3 access_key_id weedadmin
```

```bash id="n4x8ra"
dvc remote modify s3 secret_access_key weedadmin123
```

Verify the config:

```bash id="m1c5zd"
cat .dvc/config
```

It should now look like:

```ini id="b6t9yl"
[core]
    remote = s3

['remote "s3"']
    url = s3://dvc-storage
    endpointurl = http://localhost:8333
    access_key_id = weedadmin
    secret_access_key = weedadmin123
```

Now pull the dataset:

```bash id="h8r3qp"
dvc pull
```

Verify the file exists:

```bash id="w2k7nf"
ls -l data/raw/transactions.csv
```

And confirm the checksum:

```bash id="j5p1vc"
cat data/raw/transactions.csv.dvc
```

```bash id="r9m4tx"
md5sum data/raw/transactions.csv
```
