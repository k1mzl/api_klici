#API klici(spletni klici)
import requests

baseUrl = "https://www.google.com/"
klic = requests.get(baseUrl)

print(klic)
print(klic.text)#text. pridobi raw data klica

# scrape.


#API klici - ne vrača HTML - vrača JSON,XML

#baseUrl = "https://api.chucknorris.io/jokes/random"
#klic = requests.get(baseUrl)

#print(klic)

#ugotovimo , če so podatki JSON
#print(klic.text)

#ko smo 100% , da so podatki tipa JSON
#js = klic.json()
#print(js.get("value"))


#baseUrl="https://api.nationalize.io/?name="
#ime = "Luka"
#klic = requests.get(baseUrl+ime).json()
#print(klic.url) # preverimo generiran URL


#print(klic.get("count"))
#print(klic.get("name"))
#drzave =klic.get("country")

#for d in drzave:
#    print(d.get("country_id"),d.get("probability"))
    

#baseUrl = "https://auth0.com/"
#klic = requests.get(baseUrl)

#print(klic)
#print(klic.text)
#print(klic.get("Product"))