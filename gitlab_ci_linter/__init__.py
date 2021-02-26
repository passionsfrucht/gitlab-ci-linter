#!/usr/bin/env python3
import argparse
import json
import logging
import os
import ssl
import sys
import urllib.parse
import urllib.request


def parse_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--server",
        default="https://gitlab.com",
        help="This server will check .gitlab-ci.yml",
    )
    parser.add_argument(
        "--filename", default=".gitlab-ci.yml", help="Specify Gitlab CI filename"
    )
    parser.add_argument(
        "-k",
        "--insecure",
        action="store_true",
        help="Allow insecure server connections when using SSL",
    )
    parser.add_argument(
        "--private-token",
        help="Use this private token to authenticate on the server",
        default=os.environ.get("GITLAB_PRIVATE_TOKEN"),
    )
    parser.add_argument(
        "--project", help="Gitlab project private-token is authorized for",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    return gitlab_ci_linter(
        args.server, args.filename, args.insecure, args.private_token, args.project
    )


def encode(input):
    input = urllib.parse.quote(input)
    return input.replace("/", "%2F")


def gitlab_ci_linter(server, filename, insecure, private_token, project):
    try:
        gitlab_ci_content = open(filename).read()
    except FileNotFoundError:
        print(f"File not found: {filename}", file=sys.stderr)
        return 1

    if project:
        project = encode(project)
        url = f"{server}/api/v4/projects/{project}/ci/lint"
    else:
        url = f"{server}/api/v4/ci/lint"
    logging.debug(f"using {url} to validate gitlab-ci.y")
    content = {"content": gitlab_ci_content}
    data = json.dumps(content).encode("utf-8")

    r = urllib.request.Request(url, data=data)

    r.add_header("Content-Type", "application/json")

    if private_token:
        r.add_header("PRIVATE-TOKEN", private_token)

    # Verify or not server certificate
    ssl_ctx = ssl.SSLContext() if insecure else None
    with urllib.request.urlopen(r, context=ssl_ctx) as gitlab:
        if gitlab.status not in range(200, 300):
            print(f"Server said {gitlab.status}: {gitlab.url}", file=sys.stderr)
            return 1

        response_raw = gitlab.read()
        response = json.loads(response_raw.decode("utf-8"))

    if response.get("status") == "valid" or response.get("valid"):
        print(f"{filename} is valid")
        return 0
    else:
        print(f"{filename} is invalid (server: {server}):", file=sys.stderr)
        print("\n".join(response["errors"]), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
