from datetime import datetime, timedelta
from time import sleep

from api import get_domain_data, get_zone_data, add_zone_data, remove_zone_data, get_zone_edit_status

if __name__ == "__main__":
    print("Welcome to the Letsencrypt DNS01 Record setter for the CSC DomainManager!")
    print("Please enter your domain name: ")
    domain_to_query = input()
    print("Please enter your subdomain name: ")
    subdomain = input()
    if subdomain != "":
        key = f"_acme-challenge.{subdomain}"
    else:
        key = f"_acme-challenge"
    print("Please enter your challenge value from letsencrypt")
    value = input()
    get_domain_data(domain_to_query)
    get_zone_data(domain_to_query)

    # Publish record
    edit_id = add_zone_data(domain_to_query, "TXT", key, value)
    if edit_id is None:
        print("Exiting Program!")
        exit(1)

    # Wait at leaset
    time = datetime.now()
    end_time = time + timedelta(seconds=20)
    propagated = False
    while time < datetime.now() and not propagated:
        if not propagated:
            status = get_zone_edit_status(edit_id)
            if status is None:
                print("Exiting Program!")
                exit(2)
            elif status == "COMPLETED":
                propagated = True
        sleep(1)

    # Finally remove Record again
    edit_id = remove_zone_data(domain_to_query, "TXT", key, value)
    if edit_id is None:
        print("Exiting Program!")
        exit(1)

    # And inform user when change is propagated
    propagated = False
    while not propagated:
        status = get_zone_edit_status(edit_id)
        if status is None:
            print("Exiting Program!")
            exit(2)
        elif status == "PROPAGATING":
            pass
        elif status == "COMPLETED":
            propagated = True
        else:
            print("Exiting Program!")
        sleep(1)
