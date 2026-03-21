import requests

x = requests.get("https://www.zsnosovice.cz/")

print(x.text)