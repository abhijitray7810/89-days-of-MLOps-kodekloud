![image](https://github.com/abhijitray7810/89-days-of-MLOps-kodekloud/blob/d348faa8e775ae356c7cc936a0ea0db1035857ee/Day%2012%3A%20Configure%20a%20DVC%20Remote%20Storage/Screenshot%202026-05-24%20110202.png)
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
