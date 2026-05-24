```bash id="vwhqqm"
cd /root/code/fraud-detection

# Set s3 as the default remote
dvc remote default s3

# Verify configuration
cat .dvc/config

# Push the tracked data
dvc push
```

The config should then look like:

```ini id="jlwmwb"
['core']
    remote = s3

['remote "s3"']
    url = s3://dvc-storage
    endpointurl = http://localhost:8333
    access_key_id = weedadmin
    secret_access_key = weedadmin123
```

After `dvc push` completes successfully, check the SeaweedFS Filer UI under:

`/buckets/dvc-storage/files/md5/`

You should see uploaded DVC objects there.
