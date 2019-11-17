#!/usr/bin/env python3
import argparse
import json
import ssl
import sys
import urllib.request


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--server', default='https://gitlab.com')
    parser.add_argument('--filename', default='.gitlab-ci.yml')
    parser.add_argument('-k', '--insecure', action='store_true')
    return parser.parse_args()


def main():
    args = parse_args()
    return gitlab_ci_linter(args.server, args.filename, args.insecure)


def gitlab_ci_linter(server, filename, insecure):
    try:
        gitlab_ci_content = open(filename).read()
    except FileNotFoundError:
        print(f'File not found: {filename}', file=sys.stderr)
        return 1


    url = f'{server}/api/v4/ci/lint'
    content = {'content': gitlab_ci_content}
    data = json.dumps(content).encode('utf-8')
    r = urllib.request.Request(
        url, headers={'Content-Type': 'application/json'}, data=data
    )

    # Verify or not server certificate
    ssl_ctx = ssl.SSLContext() if insecure else None
    with urllib.request.urlopen(r, context=ssl_ctx) as gitlab:
        if gitlab.status not in range(200, 300):
            print(f'Server said {gitlab.status}: {gitlab.url}', file=sys.stderr)
            return 1

        response_raw = gitlab.read()
        response = json.loads(response_raw.decode('utf-8'))

    if response['status'] == 'valid':
        print(f'{filename} is valid')
        return 0
    else:
        print(f'{filename} is invalid (server: {server}):', file=sys.stderr)
        print('\n'.join(response['errors']), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
