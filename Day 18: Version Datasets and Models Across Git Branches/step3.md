
root@controlplane fraud-detection on  main ➜  git tag v1.0
git checkout -b v2-improved
dvc add data/raw/transactions.csv
dvc repro
git commit ...
git checkout main
dvc checkout
Switched to a new branch 'v2-improved'
100% Adding...|███████████████████████|1/1 [00:00, 107.41file/s]
                                                                
To track the changes with git, run:

        git add data/raw/transactions.csv.dvc

To enable auto staging, run:

        dvc config core.autostage true
'data/raw/transactions.csv.dvc' didn't change, skipping         
Stage 'process_data' didn't change, skipping                    
Stage 'split_data' didn't change, skipping                      
Data and pipelines are up to date.
error: pathspec '...' did not match any file(s) known to git
Switched to branch 'main'
Building workspace index             |7.00 [00:00, 1.41kentry/s]
Comparing indexes                    |8.00 [00:00, 4.58kentry/s]
Applying changes                      |0.00 [00:00,     ?file/s]

root@controlplane fraud-detection on  main ➜  git checkout v2-improved                                        git checkout v2-improved
cp data/raw/transactions_v2.csv data/raw/transactions.csv
cp data/raw/transactions_v2.csv data/raw/transactions.csv
dvc add data/raw/transactions.csv
dvc add data/raw/transactions.csv
dvc repro
dvc repro
git add data/raw/transactions.csv.dvc dvc.lock
git add data/raw/transactions.csv.dvc dvc.locket"
git commit -m "Use improved transactions dataset"
Switched to branch 'v2-improved'
100% Adding...|████████████████████████|1/1 [00:00, 40.33file/s]
                                                                
To track the changes with git, run:

        git add data/raw/transactions.csv.dvc

To enable auto staging, run:

        dvc config core.autostage true
'data/raw/transactions.csv.dvc' didn't change, skipping         
Running stage 'process_data':                                   
> python src/data/process_data.py
Updating lock file 'dvc.lock'                                   

Running stage 'split_data':                                     
> python src/data/split_data.py
Updating lock file 'dvc.lock'                                   

To track the changes with git, run:

        git add dvc.lock

To enable auto staging, run:

        dvc config core.autostage true
Use `dvc push` to send your updates to remote storage.
[v2-improved e3fef7e] Use improved transactions dataset
 2 files changed, 12 insertions(+), 12 deletions(-)

root@controlplane fraud-detection on  v2-improved ➜  cat data/raw/transactions.csv.dvc
outs:
- md5: bd6bde1f4b10d12c6249a2d021b57e87
  size: 723
  hash: md5
  path: transactions.csv

root@controlplane fraud-detection on  v2-improved ➜  git checkout main
dvc checkout
Switched to branch 'main'
Building workspace index             |7.00 [00:00, 1.41kentry/s]
Comparing indexes                    |8.00 [00:00, 4.39kentry/s]
Applying changes                      |4.00 [00:00, 2.88kfile/s]
M       data/processed/clean_transactions.csv
M       data/processed/test.csv
M       data/processed/train.csv
M       data/raw/transactions.csv

root@controlplane fraud-detection on  main ➜  git diff v1.0 -- data/raw/transactions.csv.dvc

root@controlplane fraud-detection on  main ➜  
