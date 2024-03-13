# Python CSC Domain Manager API

***STILL WORK IN PROGRESS!***

Python Script to do some basic usage of the CSC Domain Manager API.

Implemented mainly to make Letsencrypt DNS01 Challenge easier.

Tested with Python 3.11 but *should* work with any other current version of python.

### Usage
For now there is a configuration file you need to create under ***conf/config.toml*** with your API Key and HTTP Bearer
Token.
You can also supply this information on execution of the script via the CLI.

It is preferred to use a virtual environment!
Be sure to install all requirements before running the script!


To run the letsencrypt script use:
```
python main.py
```
or:
```
python main.py -l
```
<br>

To check if an edit is completed use: 

```
python main.py -c
```
<br>

For the help function use: 

```
python main.py -h
```
<br>

You can also run both the check and letsencrypt script, whereas the check will execute before letsencrypt, using: 

```
python main.py -c -l
```
