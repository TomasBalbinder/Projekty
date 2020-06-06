
import requests
from bs4 import BeautifulSoup
user = input("Find temperature in city: ")
search = "Weather in ", user

url = f"https://www.google.cz/search?&q={search}"

r = requests.get(url)


s = BeautifulSoup(r.text, "html.parser")
update = s.find("div", class_="BNeawe").text
print(user, update)