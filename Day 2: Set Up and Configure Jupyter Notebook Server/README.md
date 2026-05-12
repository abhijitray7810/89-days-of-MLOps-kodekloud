````markdown
# JupyterLab Configuration Fix

This project contains the corrected JupyterLab configuration for the xFusionCorp Industries data science environment.

## Requirements

The JupyterLab server must:

- Listen on port `8888`
- Bind to `0.0.0.0`
- Use `/root/notebooks/` as the notebook directory
- Run from the provided Python virtual environment

---

## Configuration File

Location:

```bash
/root/code/jupyter_lab_config.py
````

Updated configuration:

```python
c.ServerApp.token = ''
c.ServerApp.password = ''
c.ServerApp.disable_check_xsrf = True

c.ServerApp.notebook_dir = '/root/notebooks'
c.ServerApp.port = 8888
c.ServerApp.ip = '0.0.0.0'
```

---

## Create Notebook Directory

```bash
mkdir -p /root/notebooks
```

---

## Activate Virtual Environment

```bash
source /root/code/ml-env/bin/activate
```

---

## Start JupyterLab

```bash
jupyter lab --config=/root/code/jupyter_lab_config.py --allow-root --no-browser &
```

---

## Verify Server Status

Check whether JupyterLab is running:

```bash
ps -ef | grep jupyter
```

Check listening port:

```bash
ss -tulpn | grep 8888
```

Expected result:

* JupyterLab running on `0.0.0.0:8888`

---

## Notes

If an older JupyterLab instance is already running, stop it first:

```bash
pkill -f jupyter
```

Then restart the server using the command above.

```
```
