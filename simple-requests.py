"""
Simple sample script for Python requests library
Get the values of a random joke
"""

import requests
import json

print("Hello World!")

r = requests.get("https://api.icndb.com/jokes/random?limitTo=nerdy")

r = json.loads(r.content)

print(r["value"]["id"])