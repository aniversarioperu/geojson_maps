import json
import sys


if len(sys.argv) < 2:
    print "Enter district name to extract as argument"
    sys.exit(0)

name = sys.argv[1].strip()

districts = json.loads(open("districts_peru.geojson", "r").read())

f = open(name + ".geojson", "w")
for  i in districts['features']:
    for k, v in i.items():
        if i['properties']['name'] == "LIMA":
            print i
            f.write(json.dumps(i))
f.close()
