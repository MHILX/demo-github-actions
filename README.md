# Demo Github Actions 
[![GitHub Super-Linter](https://github.com/super-linter/super-linter/actions/workflows/ci.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)

---

## Reusable Workflows
Reusable workflows are standalone workflow files that can be reused across multiple repositories or workflows within the same repository. They are defined as separate YAML files and can be triggered by events or manually called by other workflows.

Here's an example of a reusable workflow (build-and-test-reusable-workflow.yml) that builds and tests a Node.js project:

```yml
name: Build & Test Reusable Workflow

on:
  push:
    branches:
      - main

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Node.js
        uses: actions/setup-node@v2
        with:
          node-version: 14

      - name: Install dependencies
        run: npm install

      - name: Build
        run: npm run build

      - name: Run tests
        run: npm test
```

This reusable workflow can be included in other workflows using the `uses` keyword, like this:

```yaml
name: Main Workflow

on:
  pull_request:
    branches:
      - main

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Run Build & Test Reusable Workflow
        uses: ./.github/workflows/build-and-test-reusable-workflow.yml
```

In this example, the main workflow includes and runs the build & test reusable workflow file, `build-and-test-reusable-workflow.yml`, by specifying the relative path to the file.

## Composite Workflows
Composite workflows allow you to create more complex workflows by combining and reusing multiple reusable workflows. They provide a way to define a high-level workflow that orchestrates the execution of multiple reusable workflows.

Here's an example of a composite workflow (composite-workflow.yml) that combines two reusable workflows:

```yaml
name: Composite Workflow

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Run Build Reusable Workflow
        uses: ./.github/workflows/build-reusable-workflow.yml

      - name: Run Test Reusable Workflow
        uses: ./.github/workflows/test-reusable-workflow2.yml
```

In this example, the composite workflow `composite-workflow.yml` includes and runs two reusable workflows (`build-reusable-workflow.yml` and `test-reusable-workflow.yml`). This allows you to define more complex CI/CD pipelines by combining the functionality of multiple reusable workflows.

Reusable and composite workflows provide flexibility, modularity, and reusability in defining your CI/CD processes within GitHub Actions. By leveraging these features, you can create efficient and maintainable workflows for your projects.

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