# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: April 10th, 2024
# This program creates a map and marks Hunter College

import folium

hunterMap = folium.Map(location=[40.75, -74.125], zoom_start=10)

folium.Marker(location=[40.768731, -73.96415], popup="Hunter College").add_to(hunterMap)

hunterMap.save(outfile="nycMap.html")
