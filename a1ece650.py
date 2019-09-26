# import sys
#
# # YOUR CODE GOES HERE
#
# def main():
#     ### YOUR MAIN CODE GOES HERE
#
#     ### sample code to read from stdin.
#     ### make sure to remove all spurious print statements as required
#     ### by the assignment
#     while True:
#         line = sys.stdin.readline()
#         if line == '':
#             break
#         print 'read a line:', line
#
#     print 'Finished reading input'
#     # return exit code 0 on successful termination
#     sys.exit(0)
#
# if __name__ == '__main__':
#     main()

import sys
import re
from commandG import intersection
# import numpy

address_db = {}

def add_address():
    street = re.compile(r"([a])(\s\"[A-Za-z\s]+\"\s)((\(\s*-?\d+\s*,\s*-?\d+\s*\)\s*)*)")
    matches = street.match(address)
    if street.match(address):
        groups = matches.groups()
        name = groups[1].strip()
        coordinate_str = re.findall(r'(\(\s*-?\d+\s*,\s*-?\d+\s*\))', groups[2])
        coordinates = []
        for coord in coordinate_str:
            coord = coord.replace('(', '').replace(')', '')
            temp_coord = coord.split(",")
            coordinates.append([int(temp_coord[0]), int(temp_coord[1])])
        if name not in address_db:
            address_db[name] = coordinates
        else:
            print ("Error: Address name already exists, use 'c' to change street")
    else:
        print ("Error: invalid command")
        pass

def change_address():
        street = re.compile(r"([c])(\s\"[A-Za-z\s]+\"\s)((\(\s*-?\d+\s*,\s*-?\d+\s*\)\s*)*)")
        matches = street.match(address)
        if street.match(address):
            groups = matches.groups()
            name = groups[1].strip()
            coordinate_str = re.findall(r'(\(\s*-?\d+\s*,\s*-?\d+\s*\))', groups[2])
            coordinates = []
            for coord in coordinate_str:
                coord = coord.replace('(', '').replace(')', '')
                temp_coord = coord.split(",")
                coordinates.append([int(temp_coord[0]), int(temp_coord[1])])
            if name in address_db:
                address_db[name] = coordinates
            else:
                print ("Error: Address not found")
        else:
            print ("Error: invalid!")
            pass


def remove_address():
    street = re.compile(r"([r])(\s\"[A-Za-z\s]+\")")
    matches = street.match(address)
    if street.match(address):
        groups = matches.groups()
        name = groups[1].strip()
        if name in address_db:
            address_db.pop(name)
        else:
            print ("Error: Address not found")
    else:
        print ("Error: invalid!")
        pass
    # else:
        # print ("Error!")

def graph():
    # Regular expression for graph
    V = []
    E = []
    num = 1
    # print address_db

    for street_a in address_db:
        coordinates = address_db[street_a]
        for i in range(len(coordinates)-1):
            # print street_a, coordinates[i], coordinates[i+1]
            for street_b in address_db:
                if street_a == street_b:
                    continue
                coordinates_b = address_db[street_b]
                for j in range(len(coordinates_b) - 1):
                     # print street_b, coordinates_b[j], coordinates_b[j + 1]
                    x1, y1 = coordinates[i][0], coordinates[i][1]
                    x2, y2 = coordinates[i+1][0], coordinates[i+1][1]
                    x3, y3 = coordinates_b[j][0], coordinates_b[j][1]
                    x4, y4 = coordinates_b[j+1][0], coordinates_b[j+1][1]
                    x, y = intersection(x1,x2,x3,x4,y1,y2,y3,y4)
                    # print 'for points a: ', coordinates[i], coordinates[i+1], ' and b: ', coordinates_b[j], coordinates_b[j+1], ' intersection is: ', x, y
                    if x is not None:
                        add_arr = [coordinates[i], coordinates[i + 1], coordinates_b[j], coordinates_b[j + 1], [x, y]]

                        # Add vertices
                        for coordinate in add_arr:
                            if coordinate not in V:
                                V.append(coordinate)

                        # Add edges
                        add_arr_index = [V.index(x)+1 for x in add_arr]

                        edge1 = sorted([add_arr_index[0], add_arr_index[4]])
                        if edge1 not in E:
                            E.append(edge1)

                        edge2 = sorted([add_arr_index[4], add_arr_index[1]])
                        if edge2 not in E:
                            E.append(edge2)

                        edge3 = sorted([add_arr_index[2], add_arr_index[4]])
                        if edge3 not in E:
                            E.append(edge3)

                        edge4 = sorted([add_arr_index[4], add_arr_index[3]])
                        if edge4 not in E:
                            E.append(edge4)

    print 'V = {'
    for index in range(len(V)):
        print index+1, ': (', V[index][0], ',', V[index][1], ')'
    print '}'

    print 'E = {'
    for edge in E:
        print '<',edge[0],',',edge[1],'>'
    print'}'


    #             for j in range(len(coordinates_b)-1):
    #

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
        elif address[0] == 'g':
            graph()
        else:
            print ("Error: please use command line")
            sys.exit(0)
