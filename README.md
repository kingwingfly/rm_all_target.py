# rm_all_targets.py
A python script to remove all Rust targets in each sub directory interactively.

# Usage
```sh
python rm_all_targets.py
```

# Caution
This script checks from `dirname(__file__)`, you may mv it to the root of directory you store your rust projects. 
```
.
├── macros_test
├── ospp
├── rbtree
└── rm_all_target.py
```
