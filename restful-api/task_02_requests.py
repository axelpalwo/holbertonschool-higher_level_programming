#!/usr/bin/python3
import requests # type: ignore
import csv

def fetch_and_print_posts():
    res = requests.get('https://jsonplaceholder.typicode.com/todos')
    print(res.status_code)
    if res.status_code == 200:
        res = res.json()
        for data in res:
            print(data.title)
    else:
        print("Error with Fetch")

def fetch_and_save_posts():
    res = requests.get('https://jsonplaceholder.typicode.com/todos')
    if res.status_code == 200:
        res = res.json()
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            for data in res:
                print({'id': data['id'], 'title': data['title'], 'body': data})
                writer.writerow({'id': data['id'], 'title': data['title'], 'body': data})
    else:
        print("Error with Fetch")
