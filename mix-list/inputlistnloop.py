#!/usr/bin/env python3

def main():
    networklists = []
    with open('driverip.txt', 'r') as driverip:
        for sline in driverip: 
            networklists.append(sline.rstrip("\n").split(' '))

    print(networklists)

    for driverandip in networklists:
        print ('SSH to ' + driverandip[1] + ' using driver ' + driverandip[0])

main()

