# check-gitlab-ci

`.gitlab-ci.yml` lint script and pre-commit.com hook.

The vetter way to use this - use as pre-commit hooks.

## Pre-commit hook
See [pre-commit](https://pre-commit.com) for instructions.
```bash
pip install pre-commit
# Feel .pre-commit-config.yaml as showed below
pre-commit install
pre-commit run --all-files
```

Sample `.pre-commit-config.yaml`:
```yaml
-   repo: https://gitlab.com/devopshq/gitlab-ci-linter
    rev: 1.0.0
    hooks:
    -   id: gitlab-ci-linter
```

To specify your own Gitlab server:
```yaml
-   repo: https://gitlab.com/devopshq/gitlab-ci-linter
    rev: 1.0.0
    hooks:
    - id: gitlab-ci-linter
      args:
        - '--server'
        - 'https://gitlab.example.com'
```
To change a filename:
```yaml
-   repo: https://gitlab.com/devopshq/gitlab-ci-linter
    rev: 1.0.0
    hooks:
    - id: gitlab-ci-linter
      files: '.gitlab-ci.custom.yml'
      args:
        - '--filename'
        - '.gitlab-ci.custom.yml'
```

## Installation
We have no package on `pypi` yet. Use git instead:

```bash
pip install git+https://gitlab.com/devopshq/gitlab-ci-linter#master
gitlab-ci-linter
```
