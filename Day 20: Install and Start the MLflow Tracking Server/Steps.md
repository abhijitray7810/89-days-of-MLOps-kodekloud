To satisfy the lab requirements on the controlplane, run:

```bash
mkdir -p /root/code/mlflow-backend
mkdir -p /root/code/mlflow-artifacts

nohup mlflow server \
  --host 0.0.0.0 \
  --port 5000 \
  --backend-store-uri sqlite:////root/code/mlflow-backend/mlflow.db \
  --artifacts-destination /root/code/mlflow-artifacts \
  --cors-allowed-origins '*' \
  --allowed-hosts '*' \
  >/root/mlflow-server.log 2>&1 &
```

Verify the server is running:

```bash
ps -ef | grep mlflow
```

Verify the database file exists:

```bash
ls -l /root/code/mlflow-backend/mlflow.db
```

Verify the port is listening on all interfaces:

```bash
ss -lntp | grep 5000
```

Expected output should show something similar to:

```text
LISTEN 0 4096 0.0.0.0:5000
```

You can also test locally:

```bash
curl http://localhost:5000
```

Using `nohup ... &` ensures the MLflow server remains running in the background after the terminal session is closed. Once these checks pass, the **MLflow UI** button should open the dashboard and show the empty **Default** experiment.
