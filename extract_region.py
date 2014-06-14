#-*- coding: utf-8 -*-
import json
import math


def convert(coordinates):
    new_coords = []
    for i in coordinates:
        for j in i[0]:
            lati = 90 + j[0]
            longi = 90 + j[1]
            new_coord = [lati, longi]
            new_coords.append(new_coord)
    return [[new_coords]]


print "All regions will be processed"

districts = json.loads(open("region.geojson", "r").read())

f = open("output.geojson", "w")

objects = []
ids = []
for  i in districts['features']:
    for k, v in i.items():
        if i['properties']['id'] not in ids:
            #longitude = str(i['geometry']['coordinates'][0][0][0][0])
            #i['properties']['longitude'] = longitude
            #latitude = str(i['geometry']['coordinates'][0][0][0][1])
            coordinates = i['geometry']['coordinates']
            i['geometry']['coordinates'] = convert(coordinates)
            #print coordinates

            objects.append(i)
            ids.append(i['properties']['id'])

out = {}
out['type'] = 'FeatureCollection'
out['features'] = objects
f.write(json.dumps(out, indent=4))
f.close()
