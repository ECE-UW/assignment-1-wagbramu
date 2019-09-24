import sys
import re
# import numpy

address_db = {}


    # datalist = []
    # if data == '':
    #     print(len(datalist))
    # else:
    #     datalist.append(data)
        # print(len(datalist))
# from typing import List, Any

# address = [a "weber" (1,2)(1,3)(1,5)(3,4)]  # type: List[address]
def add_address():
    street = re.compile(r"([a])(\s\"[A-Za-z]+\"\s)((\(-?\d+,-?\d+\))*)")
    matches = street.match(address)
    if street.match(address):
        groups = matches.groups()
        name = groups[1]
        coordinate_str = re.findall(r'(\(-?\d+,-?\d+\))', groups[2])
        coordinates = []
        for coord in coordinate_str:
            coord = coord.replace('(', '').replace(')', '')
            temp_coord = coord.split(",")
            coordinates.append([int(temp_coord[0]), int(temp_coord[1])])
        address_db[name]=coordinates
    else:
        print ("Error!")
        pass

def change_address():
        street = re.compile(r"([c])(\s\"[A-Za-z]+\"\s)((\(-?\d+,-?\d+\))*)")
        matches = street.match(address)
        if street.match(address):
            groups = matches.groups()
            name = groups[1]
            coordinate_str = re.findall(r'(\(-?\d+,-?\d+\))', groups[2])
            coordinates = []
            for coord in coordinate_str:
                coord = coord.replace('(', '').replace(')', '')
                temp_coord = coord.split(",")
                coordinates.append([int(temp_coord[0]), int(temp_coord[1])])
            if name in address_db:
                address_db[name] = coordinates
            else:
                print ("Address not found")
        else:
            print ("Error!")
            pass


def remove_address():
    street = re.compile(r"([r])(\s\"[A-Za-z]+\")")
    matches = street.match(address)
    if street.match(address):
        groups = matches.groups()
        name = groups[1]
        if name in address_db:
            address_db.pop(name)
        else:
            print ("Address not found")
    else:
        print ("Error!")
        pass
    # else:
        # print ("Error!")


if __name__ == '__main__':
    while True:
        address = sys.stdin.readline()
        if address =='':
            break
        address = address.strip()
        if address[0] == 'a':
            add_address()
        elif address[0] == 'c':
            change_address()
        elif address[0] == 'r':
            remove_address()
    #    (a|c|r|g)
    #     print

