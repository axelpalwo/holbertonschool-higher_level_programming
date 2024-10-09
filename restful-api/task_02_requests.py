#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    res = requests.get('https://jsonplaceholder.typicode.com/todos')
    print(res.status_codes)
    if res.status_codes == 'OK':
        res.json()
        for data in res:
            print(data.title)

def fetch_and_save_posts():
    res = requests.get('https://jsonplaceholder.typicode.com/todos')
    if res.status_codes == 'OK':
        for data in res:
            print({'id': data.id, 'title': data.title, 'body': data.body})
        toBeSaved = "posts.csv"
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