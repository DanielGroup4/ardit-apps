import folium
import pandas as pd

data = pd.read_csv("volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elevation = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location= [38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fgv =folium.FeatureGroup(name="Volcanoes")

for lt, ln, ele in zip(lat, lon, elevation):
    #fg.add_child(folium.Marker(location= [lt, ln], popup= str(ele) + " m", icon=folium.Icon(color= color_producer(ele))))
    fgv.add_child(folium.CircleMarker(location = [lt, ln], popup= str(ele)+" m",
    fill_color= color_producer(ele), color= "grey", fill_opacity= 0.7))

fgp =folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data= open("world.json", "r", encoding="utf-8-sig").read(), 
style_function= lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000 
else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("map1.html")      
