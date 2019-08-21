#!/usr/bin/env python

import argparse
import pprint

from enumerate_iam.main import enumerate_iam


def main():
    parser = argparse.ArgumentParser(description='Enumerate IAM permissions')

    parser.add_argument('--access-key', help='AWS access key', required=True)
    parser.add_argument('--secret-key', help='AWS secret key', required=True)
    parser.add_argument('--session-token', help='STS session token')
    parser.add_argument('--region', help='AWS region to send API requests to', default='us-east-1')
    parser.add_argument('--verbose', help='Dump output results', action='store_true', default=False)

    args = parser.parse_args()

    output = enumerate_iam(args.access_key,
                  args.secret_key,
                  args.session_token,
                  args.region)

    if args.verbose:
        pp = pprint.PrettyPrinter(indent=4)

        print('===== iam =====')
        pp.pprint(output['iam'])

        print('\n===== bruteforce =====')
        pp.pprint(output['bruteforce'])


if __name__ == '__main__':
    main()
