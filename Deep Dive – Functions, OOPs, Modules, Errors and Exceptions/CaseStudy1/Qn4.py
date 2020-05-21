# Write a program to find distance between two locations when their latitude and longitudes are given.


from math import radians, cos, sin, asin, sqrt

lat1 = 5.99
lat2 = 5.678
lon1 = 2.59
lon2 = 3.56


def distance(lat_1, lat_2, lon_1, lon_2):

    lon_1 = radians(lon_1)
    lon_2 = radians(lon_2)
    lat_1 = radians(lat_1)
    lat_2 = radians(lat_2)
    radius = 6371

    d_lon = lon_2 - lon_1
    d_lat = lat_2 - lat_1
    x = sin(d_lat / 2) ** 2 + cos(lat_1) * cos(lat_2) * sin(d_lon / 2) ** 2

    y = 2 * asin(sqrt(x))

    z = radius * y

    return z


print(distance(lat1, lat2, lon1, lon2), "K.M")
