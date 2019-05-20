import folium
import pandas
map=folium.Map(location=[],tiles="Mapbox Bright")

data=pandas.read_csv("E:\\irisu.txt",sep="\t")

lt=list(data.Lat)
ln=list(data.Lon)

print(data)
for i,j in zip(lt,ln):
    strs=(i*2,j*2)
    map.add_child(folium.Marker(location=[i*2,j*2],popup=str(strs)+"(lat,lon)",icon=folium.Icon(color="Blue")))
    print(i,j)
for i,j in zip(lt,ln):
    strs = (i*3, j*3)
    map.add_child(folium.Marker(location=[i*3,j*3],popup=str(strs)+"(lat,lon)",icon=folium.Icon(color="Blue")))
    print(i,j)
for i,j in zip(lt,ln):
    strs = (i*4, j*4)
    map.add_child(folium.Marker(location=[i*4,j*4],popup=str(strs)+"(lat,lon)",icon=folium.Icon(color="Blue")))
    print(i,j)
map.save("E:\\Map1.html")
