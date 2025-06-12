import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.tiobe.com/tiobe-index/")
bs = BeautifulSoup(resp.text, "html.parser")

table = bs.find(id = "top20")
body = table.tbody
# Take only first 10 rows
rows = body.find_all("tr")[:10]


for row in rows:
    # take all cols
    cols = row.find_all("td")
    print(f"{cols[4].text:20}  {cols[5].text}")
