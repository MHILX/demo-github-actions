# Demo Github Actions 
[![GitHub Super-Linter](https://github.com/super-linter/super-linter/actions/workflows/ci.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)

---
## To run unit test

>Test file naming convention: The unittest framework expects test files to be named with a specific naming convention. By default, test files should start with the prefix test_. For example, test_main.py.

### Option #1
```shell
 py main_test.py  
```
### Option #2
```shell
py -m unittest discover
```

This command will automatically discover and run all the unit tests within the current directory and its subdirectories.

If your test files are located in a specific directory, you can specify the directory path instead of using `discover`. For example:

```shell
python -m unittest discover -s tests
```
Replace `tests` with the actual directory name where your unit test files reside.

The unittest framework will execute all the unit tests it finds and provide output indicating the success or failure of each test case.

---
## Project dependencies
- flask
- python-dotenv