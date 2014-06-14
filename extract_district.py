#-*- coding: utf-8 -*-
import json
import sys


names = ["LIMA", "SAN MARTIN DE PORRES", "ANCON", "ATE", "BARRANCO", u"BREÑA",
        "CARABAYLLO", "CHACLACAYO", "CHORRILLOS", "CIENEGUILLA", "COMAS",
        "EL AGUSTINO", "INDEPENDENCIA", "JESUS MARIA", "LA MOLINA",
        "LA VICTORIA", "LINCE", "LOS OLIVOS", "LURIGANCHO", "LURIN", 
        "MAGDALENA DEL MAR", "MIRAFLORES", "PACHACAMAC", "PUCUSANA", 
        "PUEBLO LIBRE", "PUENTE PIEDRA", "PUNTA HERMOSA", "PUNTA NEGRA",
        "RIMAC", "SAN BARTOLO", "SAN BORJA", "SAN ISIDRO", 
        "SAN JUAN DE LURIGANCHO", "SAN LUIS", "SAN MIGUEL", "SANTA ANITA",
        "SANTA ROSA", "SANTIAGO DE SURCO", "SURQUILLO", "VILLA EL SALVADOR",
        "VILLA MARIA DEL TRIUNFO"]

if len(sys.argv) < 2:
    print "Enter ubigeo as argument (only three first digits)"
    sys.exit(0)

print "Districts are harcoded in list ``names``", names
ubigeo = str(sys.argv[1].strip())

districts = json.loads(open("districts_peru.geojson", "r").read())

f = open("output.geojson", "w")

objects = []
ids = []
for  i in districts['features']:
    for k, v in i.items():
        if i['properties']['name'] in names \
                and i['properties']['id'] not in ids \
                and i['properties']['ubigeo'].startswith(ubigeo):
            objects.append(i)
            ids.append(i['properties']['id'])

out = {}
out['type'] = 'FeatureCollection'
out['features'] = objects
f.write(json.dumps(out, indent=4))
f.close()
