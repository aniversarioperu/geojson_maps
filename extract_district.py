#-*- coding: utf-8 -*-
import json


names = [
    "LIMA", "ANCON", "ATE", "BARRANCO", u"BREÑA", "CARABAYLLO",
    "CHACLACAYO", "CHORRILLOS", "CIENEGUILLA", "COMAS", "EL AGUSTINO",
    "INDEPENDENCIA", "JESUS MARIA", "LA MOLINA", "LA VICTORIA", "LINCE",
    "LOS OLIVOS", "LURIGANCHO", "LURIN", "MAGDALENA DEL MAR", 
    "MAGDALENA VIEJA", "MIRAFLORES",
    "PACHACAMAC", "PUCUSANA", "PUEBLO LIBRE", "PUENTE PIEDRA", "PUNTA HERMOSA",
    "PUNTA NEGRA", "RIMAC", "SAN BARTOLO", "SAN BORJA", "SAN ISIDRO",
    "SAN JUAN DE LURIGANCHO", "SAN MARTIN DE PORRES",
    "SAN JUAN DE MIRAFLORES", "SAN LUIS", "SAN MIGUEL",
    "SANTA ANITA", "SANTA ROSA", "SANTIAGO DE SURCO", "SURQUILLO", 
    "VILLA EL SALVADOR", "VILLA MARIA DEL TRIUNFO",
    "BELLAVISTA", "LA PERLA", "CALLAO", "VENTANILLA", 
    "CARMEN DE LA LEGUA REYNOSO", "LA PUNTA",
]


ubigeos = ["1501", "0701"]
print "Districts are harcoded in list ``names``", names
print "Ubigeos are harcoded in list ``ubigeos`` (only first 4 digits)", ubigeos

districts = json.loads(open("districts_peru.geojson", "r").read())

f = open("output.geojson", "w")

objects = []
ids = []
for  i in districts['features']:
    for k, v in i.items():
        if i['properties']['name'] in names \
                and i['properties']['id'] not in ids \
                and i['properties']['ubigeo'][0:4] in ubigeos:
            objects.append(i)
            ids.append(i['properties']['id'])

out = {}
out['type'] = 'FeatureCollection'
out['features'] = objects
f.write(json.dumps(out, indent=4))
f.close()
