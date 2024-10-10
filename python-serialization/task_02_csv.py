#!/usr/bin/python3
import csv 
import json

def convert_csv_to_json(filename):
    toBeSaved = "data.json"
    data = []
    try:
        with open(filename, encoding='utf-8') as f:
            csvReader = csv.DictReader(f)

            for row in csvReader:
                data.append(row)

        with open(toBeSaved, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(data))

        return True
    except FileNotFoundError:
        return False
