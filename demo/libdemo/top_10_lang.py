import requests

resp = requests.get("https://www.tiobe.com/tiobe-index/")

print(resp.text)
