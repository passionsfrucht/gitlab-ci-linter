<!-- Empty lines are removed in gitlab ide, but TOC-generator requires them -->

<!-- toc -->

- [gitlab-ci-linter](#gitlab-ci-linter)
  * [Install](#install)
  * [Pre-commit hook](#pre-commit-hook)

<!-- tocstop -->

# gitlab-ci-linter

`.gitlab-ci.yml` lint script and pre-commit.com hook.

The better way to use it - use as pre-commit hooks.
## Install
We have no package on `pypi` yet. Use git instead:

```bash
cd yourproject

pip install git+https://gitlab.com/devopshq/gitlab-ci-linter#master
gitlab-ci-linter --help

#
gitlab-ci-linter

# Check with your on-premise instanse
gitlab-ci-linter --server https://gitlab.example.com #--insecure --private-token <GITLAB_PRIVATE_TOKEN>
```

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
    rev: v1.0.2
    hooks:
    -   id: gitlab-ci-linter
```

To specify your own Gitlab server:
```yaml
-   repo: https://gitlab.com/devopshq/gitlab-ci-linter
    rev: v1.0.2
    hooks:
    - id: gitlab-ci-linter
      args:
        - '--server'
        - 'https://gitlab.example.com'
# Use --insecure for self-signed certificate if you don't worry about security :)
# Or if you have a error: [SSL: CERTIFICATE_VERIFY_FAILED]
#        - '--insecure'
# Set GITLAB_PRIVATE_TOKEN to a project access token with `api` scope as environment variable to authenticate on your own
# Gitlab server
```
To change a filename:
```yaml
-   repo: https://gitlab.com/devopshq/gitlab-ci-linter
    rev: v1.0.2
    hooks:
    - id: gitlab-ci-linter
      files: '.gitlab-ci.custom.yml'
      args:
        - '--filename'
        - '.gitlab-ci.custom.yml'
```


To use a project specific api endpoint:
```yaml
-   repo: https://gitlab.com/devopshq/gitlab-ci-linter
    rev: v1.0.2
    hooks:
    - id: gitlab-ci-linter
      files: '.gitlab-ci.custom.yml'
      args:
        - '--server'
        - 'https://gitlab.example.com'
        - '--project'
        - 'user-name/my-project'
```

-----
Inspired by https://gitlab.com/smop/pre-commit-hooks
