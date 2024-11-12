import googlemaps

gmaps = googlemaps.Client(key='AIzaSyAIjtjj4K4BSSGPbykWzQdcpS9kmvcviw8')

def road_distance(coord1, coord2):
    directions = gmaps.directions(coord1, coord2, mode="driving")
    print(directions)
    distance = directions[0]['legs'][0]['distance']['value'] / 1000  # em quilômetros
    return distance

coord1 = "Avenida Fernandes Lima, 1000 - Maceió, AL"
coord2 = "Avenida Napoleão Viana de Oliveira, 87 - Rio Largo, AL"
dist = road_distance(coord1, coord2)
print(f"Distância por estrada: {dist} km")