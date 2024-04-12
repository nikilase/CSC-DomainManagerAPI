import argparse

from app import push_letsencrypt, check_status
from app.api import get_domains

parser = argparse.ArgumentParser(
    description="Run tool for CSC Domain Manager API and Letsencrypt Script."
)
parser.add_argument(
    "-l",
    "--letsencrypt",
    action="store_true",
    help="Run the Letsencrypt Script. (default run type)",
)
parser.add_argument(
    "-c",
    "--check",
    action="store_true",
    help="Check the status of the domain. Runs before letsencrypt.",
)

parser.add_argument(
    "-d",
    "--domains",
    action="store_true",
    help="Function that can be used to see all domains. Also useful to run every week so that the API Token does not "
    "get inactive (after 30 days of no use).",
)
args = parser.parse_args()
print("―" * 20)
no_arg = True

if args.domains:
    no_arg = False
    get_domains()
    print("―" * 20)

if args.check:
    no_arg = False
    check_status.main()
    print("―" * 20)

if args.letsencrypt:
    no_arg = False
    push_letsencrypt.main()
    print("―" * 20)

if no_arg:
    push_letsencrypt.main()
    print("―" * 20)
