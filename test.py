
import subprocess
import os
import json
from utils import battery_id

with open('batteries.json', 'r') as file: 
    batteries = json.load(file)
    for battery in batteries:
        print('Testing', battery['brand'], battery['model'])
        assert battery['brand']
        assert battery['model']
        assert battery['chemistry']
        assert battery['size']
        assert battery['capacity']
        assert battery['voltage']
        assert battery['stableCurrent']
        assert battery['maxVapingCurrent']
        assert battery['cutOff']
        assert battery['imgUrl']
        assert battery['reviewUrl']


