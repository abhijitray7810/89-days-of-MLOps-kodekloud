root@controlplane ~/code via 🐍 v3.12.3 ✖ cat /root/code/jupyter_lab_config.py 
# Jupyter configuration file for the xFusionCorp Industries data science team

# --- xFusionCorp team overrides (review before starting the server) ---
c.ServerApp.token = ''
c.ServerApp.password = ''
c.ServerApp.disable_check_xsrf = True
c.ServerApp.notebook_dir = '/root/wrong-path'
c.ServerApp.port = 8000
c.ServerApp.ip = '1.1.1.1'

root@controlplane ~/code via 🐍 v3.12.3 ➜  mkdir -p /root/notebooks

root@controlplane ~/code via 🐍 v3.12.3 ➜  vi /root/code/jupyter_lab_config.py 

root@controlplane ~/code via 🐍 v3.12.3 ➜  source /root/code/ml-env/activate
bash: /root/code/ml-env/activate: No such file or directory

root@controlplane ~/code via 🐍 v3.12.3 ✖ source /root/code/ml-env/bin/activate

root@controlplane ~/code via 🐍 v3.12.3 (ml-env) ➜  jupyter lab --config=/root/code/jupyter_lab_config.py --allow-root --no-browser &
[1] 5300

root@controlplane ~/code via 🐍 v3.12.3 (ml-env) ✦ ➜  [W 2026-05-12 10:53:29.595 ServerApp] ServerApp.token config is deprecated in 2.0. Use IdentityProvider.token.
[W 2026-05-12 10:53:29.613 ServerApp] notebook | error adding extension (enabled: True): The module 'notebook' could not be found (No module named 'notebook'). Are you sure the extension is installed?
    Traceback (most recent call last):
      File "/root/code/ml-env/lib/python3.12/site-packages/jupyter_server/extension/manager.py", line 365, in add_extension
        extpkg = ExtensionPackage(name=extension_name, enabled=enabled)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/root/code/ml-env/lib/python3.12/site-packages/jupyter_server/extension/manager.py", line 219, in __init__
        self._load_metadata()
      File "/root/code/ml-env/lib/python3.12/site-packages/jupyter_server/extension/manager.py", line 234, in _load_metadata
        raise ExtensionModuleNotFound(msg) from None
    jupyter_server.extension.utils.ExtensionModuleNotFound: The module 'notebook' could not be found (No module named 'notebook'). Are you sure the extension is installed?
[I 2026-05-12 10:53:29.614 ServerApp] jupyter_lsp | extension was successfully linked.
[I 2026-05-12 10:53:29.616 ServerApp] jupyter_server_terminals | extension was successfully linked.
[I 2026-05-12 10:53:29.619 ServerApp] jupyterlab | extension was successfully linked.
[I 2026-05-12 10:53:29.619 ServerApp] Writing Jupyter server cookie secret to /root/.local/share/jupyter/runtime/jupyter_cookie_secret
[I 2026-05-12 10:53:29.827 ServerApp] notebook_shim | extension was successfully linked.
[W 2026-05-12 10:53:29.836 ServerApp] All authentication is disabled.  Anyone who can connect to this server will be able to run code.
[I 2026-05-12 10:53:29.837 ServerApp] notebook_shim | extension was successfully loaded.
[I 2026-05-12 10:53:29.838 ServerApp] jupyter_lsp | extension was successfully loaded.
[I 2026-05-12 10:53:29.838 ServerApp] jupyter_server_terminals | extension was successfully loaded.
[I 2026-05-12 10:53:29.840 LabApp] JupyterLab extension loaded from /root/code/ml-env/lib/python3.12/site-packages/jupyterlab
[I 2026-05-12 10:53:29.840 LabApp] JupyterLab application directory is /root/code/ml-env/share/jupyter/lab
[I 2026-05-12 10:53:29.840 LabApp] Extension Manager is 'pypi'.
[I 2026-05-12 10:53:29.864 ServerApp] jupyterlab | extension was successfully loaded.
[I 2026-05-12 10:53:29.865 ServerApp] Serving notebooks from local directory: /root/notebooks
[I 2026-05-12 10:53:29.865 ServerApp] Jupyter Server 2.18.2 is running at:
[I 2026-05-12 10:53:29.865 ServerApp] http://controlplane:8888/lab
[I 2026-05-12 10:53:29.865 ServerApp]     http://127.0.0.1:8888/lab
[I 2026-05-12 10:53:29.865 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[I 2026-05-12 10:53:30.195 ServerApp] Skipped non-installed server(s): basedpyright, bash-language-server, dockerfile-language-server-nodejs, javascript-typescript-langserver, jedi-language-server, julia-language-server, pyrefly, pyright, python-language-server, python-lsp-server, r-languageserver, sql-language-server, texlab, typescript-language-server, unified-language-server, vscode-css-languageserver-bin, vscode-html-languageserver-bin,
root@controlplane ~/code via 🐍 v3.12.3 (ml-env) ✦ ➜  ss -tulnp | grep 8888
tcp   LISTEN 0      128          0.0.0.0:8888      0.0.0.0:*    users:(("jupyter-lab",pid=5300,fd=6))                                                                                                                                                                                                                                                                                                                                                                          

root@controlplane ~/code via 🐍 v3.12.3 (ml-env) ✦ ➜  [I 2026-05-12 10:55:46.924 ServerApp] 302 GET / (@10.244.97.161) 0.42ms
[W 2026-05-12 10:56:05.314 LabApp] Could not determine jupyterlab build status without nodejs
[W 2026-05-12 10:56:34.316 LabApp] Could not determine jupyterlab build status without nodejs
root@controlplane ~/code via 🐍 v3.12.3 (ml-env) ✦ ➜  
