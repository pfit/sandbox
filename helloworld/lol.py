import requests

URL = "https://www.fantasyfootballnerd.com/service/players/xml/bx6tggrzinkc/rb/"

response = requests.get(URL)
with open('runningbacks.xml', 'wb') as f:
    f.write(response.content)
