import xml.etree.ElementTree as ET
import json
from utils import battery_id, normalize_chemistry_and_name

tree = ET.parse('/Users/stasbar/Projects/AndroidProjects/Vape-Tool-Android/app/src/main/res/values/batteries.xml')
imgspath = '/Users/stasbar/Projects/AndroidProjects/Vape-Tool-Android/app/src/main/res/drawable/'
root = tree.getroot()
print(root.tag)
batterylist = root.findall(".//*[@name='batteryList']/item")
batteryimgpath = root.findall(".//*[@name='batteryImgPath']/item")
batteries = list()

for index, child in enumerate(batterylist):
    brand, model, size, capacity, voltage, stable, maxvaping, cutoff, review, *tail = child.text.split(";")
    imgname = batteryimgpath[index].text[10:]
    battery = {
            "brand": brand,
            "model": model,
            "size": size,
            "chemistry": '',
            "capacity": int(capacity),
            "voltage": float(voltage),
            "stableCurrent": float(stable),
            "maxVapingCurrent": float(maxvaping),
            "cutOff": float(cutoff),
            "reviewUrl": review,
            "imgUrl": f'{imgspath}{imgname}.webp',
            }
    normalize_chemistry_and_name(battery)
    batteries.append(battery)

batteries.sort(key=lambda b: battery_id(b).lower())
print(batteries)
with open('batteries.json','w') as file:
    json.dump(batteries, file, indent=4)
