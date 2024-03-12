import argparse

from app import push_letsencrypt, check_status

parser = argparse.ArgumentParser(description='Run tool for CSC Domain Manager API and Letsencrypt Script.')
parser.add_argument('-l', '--letsencrypt', action='store_true',
                    help='Run the Letsencrypt Script. (default run type)')
parser.add_argument('-c', '--check', action='store_true',
                    help='Check the status of the domain. Runs before letsencrypt.')
args = parser.parse_args()
print('―' * 20)
no_arg = True

if args.check:
    no_arg = False
    check_status.main()
    print('―' * 20)

if args.letsencrypt:
    no_arg = False
    push_letsencrypt.main()
    print('―' * 20)

if no_arg:
    push_letsencrypt.main()
    print('―' * 20)
