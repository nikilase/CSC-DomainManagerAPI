# Python CSC Domain Manager API

***STILL WORK IN PROGRESS!***

Python Script to do some basic usage of the CSC Domain Manager API.

Implemented mainly to make Letsencrypt DNS01 Challenge easier.

Tested with Python 3.11 but *should* work with any other current version of python.

### Usage

For now there is a configuration file you need to create und ***conf/config.toml*** with your API Key and HTTP Bearer
Token.

Then just run the prototype script to get some basic info about your CSC Tenant and the domain you queried. 