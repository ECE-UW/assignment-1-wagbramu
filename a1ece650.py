import sys
import re
from commandG import intersection
from commandG import caldist
from commandG import on_segment

address_db = {}
address = None

def add_address():
    street = re.compile(r"([a])(\s\"[A-Za-z\s]+\"\s)((\(\s*-?\d+\s*,\s*-?\d+\s*\)\s*)*)")
    matches = street.match(address)
    if street.match(address):
        groups = matches.groups()
        name = groups[1].strip().lower()
        # name_str = re.findall(r'(\s\"[A-Za-z\s]+\"\s)')
        # for nam in
        coordinate_str = re.findall(r'(\(\s*-?\d+\s*,\s*-?\d+\s*\))', groups[2])
        coordinates = []
        for coord in coordinate_str:
            coord = coord.replace('(', '').replace(')', '')
            temp_coord = coord.split(",")
            coordinates.append([int(temp_coord[0]), int(temp_coord[1])])
        if name not in address_db:
            address_db[name] = coordinates
        else:
            print >> sys.stderr, "Error: Address name already exists, use 'c' to change street"
    else:
        print >> sys.stderr, "Error: Make Sure inputs are valid"
        pass

def change_address():
        street = re.compile(r"([c])(\s\"[A-Za-z\s]+\"\s)((\(\s*-?\d+\s*,\s*-?\d+\s*\)\s*)*)")
        matches = street.match(address)
        if street.match(address):
            groups = matches.groups()
            name = groups[1].strip().lower()
            coordinate_str = re.findall(r'(\(\s*-?\d+\s*,\s*-?\d+\s*\))', groups[2])
            coordinates = []
            for coord in coordinate_str:
                coord = coord.replace('(', '').replace(')', '')
                temp_coord = coord.split(",")
                coordinates.append([int(temp_coord[0]), int(temp_coord[1])])
            if name in address_db:
                address_db[name] = coordinates
            else:
                print >> sys.stderr, "Error: Address not found"
        else:
            print >> sys.stderr, "Error: invalid!"
            pass

def remove_address():
    street = re.compile(r"([r])(\s\"[A-Za-z\s]+\")")
    matches = street.match(address)
    if street.match(address):
        groups = matches.groups()
        name = groups[1].strip().lower()
        if name in address_db:
            address_db.pop(name)
        else:
            print >> sys.stderr, "Error: Address not found"
    else:
        print >> sys.stderr, "Error: invalid command"
        pass

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

    for street_a in address_db:
        coordinates = address_db[street_a]
        for i in range(len(coordinates) - 1):
            # print street_a, coordinates[i], coordinates[i+1]
            for street_b in address_db:
                if street_a == street_b:
                    continue
                coordinates_b = address_db[street_b]
                for j in range(len(coordinates_b) - 1):
                    x1, y1 = coordinates[i][0], coordinates[i][1]
                    x2, y2 = coordinates[i + 1][0], coordinates[i + 1][1]
                    x3, y3 = coordinates_b[j][0], coordinates_b[j][1]
                    x4, y4 = coordinates_b[j + 1][0], coordinates_b[j + 1][1]
                    x, y = intersection(x1, x2, x3, x4, y1, y2, y3, y4)
                    # print 'for points a: ', coordinates[i], coordinates[i+1], ' and b: ', coordinates_b[j], coordinates_b[j+1], ' intersection is: ', x, y
                    if x is not None:
                        add_arr = [coordinates[i], coordinates[i + 1], coordinates_b[j], coordinates_b[j + 1], [x, y]]
                        # Add edges
                        min_vert = None
                        min_dist = float("inf")
                        add_arr_index = [V.index(xi)+1 for xi in add_arr]

                        for v in V:
                            if v[0] == x and v[1] == y:
                                continue
                            if on_segment(x1,x,y1,y,v[0],v[1]):
                                if caldist(x,y,v[0],v[1]) < min_dist:
                                    min_dist = caldist(x,y,v[0],v[1])
                                    min_vert = v

                        edge1 = sorted([V.index(min_vert)+1, add_arr_index[4]])
                        if edge1 not in E:
                            E.append(edge1)


                        min_vert = None
                        min_dist = float("inf")

                        for v in V:
                            if v[0] == x and v[1] == y:
                                continue

                            if on_segment(x2, x, y2, y, v[0], v[1]):

                                if caldist(x, y, v[0], v[1]) < min_dist:
                                    min_dist = caldist(x, y, v[0], v[1])
                                    min_vert = v
                        edge2 = sorted([add_arr_index[4], V.index(min_vert)+1])
                        if edge2 not in E:
                            E.append(edge2)


                        min_vert = None
                        min_dist = float("inf")
                        for v in V:
                            if v[0] == x and v[1] == y:
                                continue
                            if on_segment(x3, x, y3, y, v[0], v[1]):
                                if caldist(x, y, v[0], v[1]) < min_dist:
                                    min_dist = caldist(x, y, v[0], v[1])
                                    min_vert = v
                        edge3 = sorted([V.index(min_vert)+1, add_arr_index[4]])
                        if edge3 not in E:
                            E.append(edge3)



                        min_vert = None
                        min_dist = float("inf")
                        for v in V:
                            if v[0] == x and v[1] == y:
                                continue
                            if on_segment(x4, x, y4, y, v[0], v[1]):
                                if caldist(x, y, v[0], v[1]) < min_dist:
                                    min_dist = caldist(x, y, v[0], v[1])
                                    min_vert = v
                        edge4 = sorted([add_arr_index[4], V.index(min_vert)+1])
                        if edge4 not in E:
                            E.append(edge4)

    print 'V = {'
    for index in range(len(V)):
        print('{0}: ({1},{2})'.format(index+1, V[index][0], V[index][1]))
    # print index+1, ': (',V[index][0],',',V[index][1],')' --- changed format to the above to eliminate spaces
    print '}'

    # print("}")
    print 'E = {'
    for edge in E:
        # print '<',edge[0],',',edge[1],'>'
        print ("<{0},{1}>".format(edge[0],edge[1]))
    print '}'


def main():
    global address
    while True:
        address = sys.stdin.readline()
        if address == '' or address[0] == '\n':
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
            print >> sys.stderr, "Error: please use command line"
    sys.exit(0)
if __name__ == '__main__':
    main()



