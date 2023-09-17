import math

def haversine(lat2, lon2):
    # Radius of the Earth in kilometers
    lat1, lon1 = 47.3769, 8.5417  # Zurich
    R = 6371.0

    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Differences in coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Haversine formula 
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance in kilometers
    distance = R * c

    return distance

# # Example usage
# lat1, lon1 = 47.3769, 8.5417  # Zurich
# lat2, lon2 = 46.818969977782444, 9.265090034393324   # Paris
# print(haversine(lat1, lon1, lat2, lon2), "km")




