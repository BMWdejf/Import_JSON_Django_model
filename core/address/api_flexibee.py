import requests
from .models import Adresar

# GET URL address JSON file
response = requests.get("https://demo.flexibee.eu/c/demo/adresar.json")

data = response.json()['winstrom']['adresar']

for i in data:
    for_kod = i['kod']
    for_nazev = i['nazev']

    adresar = Adresar(kod=for_kod, nazev=for_nazev)
    adresar.save()