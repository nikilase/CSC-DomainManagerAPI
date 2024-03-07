from api import get_domain_data, get_zone_data

if __name__ == "__main__":
    print("Welcome to the Letsencrypt DNS01 Record setter for the CSC DomainManager!")
    print("Please enter your domain name: ")
    domain_to_query = input()
    key = "_acme-challenge"
    print("Please enter your challenge value from letsencrypt")
    value = input()
    get_domain_data(domain_to_query)
    get_zone_data(domain_to_query)