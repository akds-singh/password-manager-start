import json

try:
 with open('file.json') as f:
        data = json.load(f)
except ValueError:
    data = {}