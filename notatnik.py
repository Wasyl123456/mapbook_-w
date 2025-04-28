import requests
from bs4 import BeautifulSoup
import folium

users: list=[
    {"name":"lukasz","location":"Warszawa","posts": 89},
    {"name":"michal","location":"Dębica","posts": 10 },
    {"name":"weronika","location":"Opole","posts": 20 },
    {"name":"sabina","location":"Opoczno","posts": 25 },

]

def get_coordinates(city_name: str) ->list:
    address_url:str=f"https://pl.wikipedia.org/wiki/{city_name}"
    response = requests.get(address_url).text
    response_html = BeautifulSoup(response, "html.parser")
    longitude:float=float(response_html.select(".longitude")[1].text.replace(",","."))
    # print(longitude)
    latitude:float=float(response_html.select(".latitude")[1].text.replace(",","."))
    # print(latitude)
    return [latitude,longitude]


def get_map(users_data:list)->None:
mapa= folium.Map([52.3,21.00], zoom_start=6)
for user in users_data:
    folium.Marker(
        location=get_coordinates(city_name=user["location"]),
        popup=f'{user["name"]}<br/>{user["location"]}<br/> {user["posts"]}<br/v'
            f'<img src="{user["picture"]}" alt="{user["picture"]}"/>'
    ).add_to(mapa)

mapa.save("mapa.html")


get_map(users)



