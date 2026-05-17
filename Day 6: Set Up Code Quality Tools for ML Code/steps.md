```
cd /root/code/fraud-detection
sed -i -e '$a\' src/data/process_data.py
sed -i -e '$a\' src/models/train.py
ruff check src/
black --check src/
```
