#!/usr/bin/python3

import urllib.request
import json

MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    groundctrl = urllib.request.urlopen(MAJORTOM)

    helmet = groundctrl.read()

    helmetson = json.loads(helmet.decode('utf-8'))

    print("\n\nConverted python data")
    print(helmetson)

    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    print(people)
    for i in people:
        print(i['name'], "on the", i['craft'])
main()
