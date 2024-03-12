from datetime import datetime, timedelta
from time import sleep

import click

from api import get_domain_data, get_zone_data, add_zone_data, remove_zone_data, get_zone_edit_status, get_last_zone_edit_status


def wait_status_ok(edit_id: str) -> bool:
    i = 1
    while True:
        status = get_zone_edit_status(edit_id)

        if status is None:
            print("No Status Found!")
            return False
        elif status == "PROPAGATING" or status == "PROCESSING":
            if i >= 30:
                i = 0
                print(".")
            else:
                print(".", end="")
            i += 1
        elif status == "COMPLETED":
            return True
        else:
            print(f"GOT STATUS: {status}")
            return False
        sleep(1)


def main():
    print("Welcome to the Letsencrypt DNS01 Record setter for the CSC DomainManager!")
    print("Please enter your domain name: ")
    domain_to_query = input()
    print("Please enter your subdomain name, if applicable: ")
    subdomain = input()
    if subdomain != "":
        key = f"_acme-challenge.{subdomain}"
    else:
        key = f"_acme-challenge"
    print("Please enter your challenge value from letsencrypt")
    value = input()

    # Debug info
    #get_domain_data(domain_to_query)
    #get_zone_data(domain_to_query)

    # Wait, if other changes are propagating
    edit_id, status = get_last_zone_edit_status(domain_to_query)
    if status == "PROPAGATING":
        print("Other changes are currently propagating! Waiting till they are finished")
        propagated = wait_status_ok(edit_id)
        if not propagated:
            print("Something went wrong with the Propagating edit!")
    elif status == "COMPLETED":
        pass
    else:
        print(f"Changes are currently existing with Status {status}! Exiting!")
        exit(21)

    # Publish record
    edit_id = add_zone_data(domain_to_query, "TXT", key, value)
    if edit_id is None:
        print("Exiting Program!")
        exit(1)

    # Wait until changes are propagated
    time = datetime.now()
    end_time = time + timedelta(seconds=20)

    propagated = wait_status_ok(edit_id)
    while not click.confirm('Changes Propagated, do you want to continue with the deletion?', default=True):
        pass

    # Finally remove Record again
    edit_id = remove_zone_data(domain_to_query, "TXT", key, value)
    if edit_id is None:
        print("Exiting Program!")
        exit(1)

    # And inform user when change is propagated
    if wait_status_ok(edit_id):
        print("Successfully did all changes!")
    else:
        print("Something went wrong with the purge request!")


if __name__ == "__main__":
    main()
