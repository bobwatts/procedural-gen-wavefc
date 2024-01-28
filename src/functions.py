import sys

def set_intersect_weighted(a, b):
    ans = []
    for a_c in a:
        if a_c in b:
            for _ in range(b.count(a_c)):
                ans.append(a_c)
    return ans

def _enumerate_origin(ori_x, ori_y, x, y):
    if x == y and x < 0:
        return (x + 1, y)
    if x == y and x > 0:
        return (x - 1, y)
    if x == -y and x < 0:
        return (x - 1, y)
    if x == -y and x > 0:
        return (x, y + 1)
    if abs(x) > abs(y) and x < 0:
        return (x, y - 1)
    if abs(x) > abs(y) and x > 0:
        return (x, y + 1)
    if abs(x) < abs(y) and y < 0:
        return (x + 1, y)
    if abs(x) < abs(y) and y > 0:
        return (x - 1, y)
    if x == ori_x and y == ori_y:
        return (x - 1, y)

def _enumerate_corner(ori_x, ori_y, x, y, quad, dim):
    # m = (dim - 1) // 2
    if quad == 1:
        n_edge = [ (xi, ori_y) for xi in range(ori_x-dim+1, ori_x+1) ]
        s_edge = [(xi, ori_y-dim+1) for xi in range(ori_x-dim+1, ori_x+1)]
        e_edge = [(ori_x, yi) for yi in range(ori_y-dim+1, ori_y+1)]
        w_edge = [(ori_x-dim+1, yi) for yi in range(ori_y-dim+1, ori_y+1)]
        if x == ori_x and y == ori_y:
            return (x - 1, y)
        elif (x,y) in s_edge:
            return w_edge[s_edge.index((x,y)) - 1]
        elif (x,y) in e_edge:
            return n_edge[e_edge.index((x,y)) - 1]
        else:
            return (x + 1, y - 1)
    elif quad == 2:
        n_edge = [ (xi, ori_y) for xi in range(ori_x, ori_x+dim) ]
        s_edge = [(xi, ori_y-dim+1) for xi in range(ori_x, ori_x+dim)]
        e_edge = [(ori_x+dim-1, yi) for yi in range(ori_y-dim+1, ori_y+1)]
        w_edge = [(ori_x, yi) for yi in range(ori_y-dim+1, ori_y+1)]
        if x == ori_x and y == ori_y:
            return (x + 1, y)
        elif (x,y) in s_edge:
            return e_edge[dim - s_edge.index((x,y)) - 2]
        elif (x,y) in w_edge:
            return n_edge[dim - w_edge.index((x,y))]
        else:
            return (x - 1, y - 1)
    elif quad == 3:
        n_edge = [ (xi, ori_y+dim-1) for xi in range(ori_x, ori_x+dim) ]
        s_edge = [(xi, ori_y) for xi in range(ori_x, ori_x+dim)]
        e_edge = [(ori_x+dim-1, yi) for yi in range(ori_y, ori_y+dim)]
        w_edge = [(ori_x, yi) for yi in range(ori_y, ori_y+dim)]
        if x == ori_x and y == ori_y:
            return (x + 1, y)
        elif (x,y) in n_edge:
            return e_edge[n_edge.index((x,y)) + 1]
        elif (x,y) in w_edge:
            return s_edge[w_edge.index((x,y)) + 1]
        else:
            return (x - 1, y + 1)
    elif quad == 4:
        # (-1,1) (0,1) (1,1)
        # (-1,0) (0,0) (1,0)
        # (-1,-1) (0,-1) (1, -1)
        n_edge = [ (xi, ori_y+dim-1) for xi in range(ori_x-dim+1, ori_x+1) ]
        s_edge = [(xi, ori_y) for xi in range(ori_x-dim+1, ori_x+1)]
        e_edge = [(ori_x, yi) for yi in range(ori_y, ori_y+dim)]
        w_edge = [(ori_x-dim+1, yi) for yi in range(ori_y, ori_y+dim)]
        # print("n:" + str(n_edge))
        # print(s_edge)
        # print(e_edge)
        # print(w_edge)
        if x == ori_x and y == ori_y:
            return (x - 1, y)
        elif (x,y) in n_edge:
            # return w_edge[dim - n_edge.index((x,y))]
            return w_edge[dim - n_edge.index((x,y))]
        elif (x,y) in e_edge:
            # print("hi")
            return s_edge[dim - e_edge.index((x,y)) - 2]
        else:
            return (x + 1, y + 1)
        
def scale_biome_rarity(arules, biome, scaling_factor):
    if list(arules.keys()).count(biome) == 0:
        print("Error, biome doesn't exist - scale")
    else:
        ret = arules
        for b in arules:
            if arules[b].count(biome) >= 1:
                for _ in range(arules[b].count(biome) * scaling_factor):
                    ret[b].append(biome)
        return ret

def scale_down_biome_rarity(arules, biome, scaling_factor):
    if list(arules.keys()).count(biome) == 0:
        print("Error, biome doesn't exist - scale down")
    else:
        ret = {}
        for b in arules:
            ret[b] = []
            if biome in arules[b]:
                for i in arules[b]:
                    if i == biome:
                        ret[b].append(i)
                    else:
                        for _ in range(scaling_factor):
                            ret[b].append(i)
            else:
                ret[b] = arules[b]
        return ret

def scale_specfic_biome(arules, src_biome, target_biome, scaling_factor):
    if list(arules.keys()).count(src_biome) == 0:
        print(
            "Error, biome doesn't exist - scale specific - src doesnt exist: "
            + src_biome
        )
    elif list(arules.keys()).count(target_biome) == 0:
        print(
            "Error, biome doesn't exist - scale specific - target doesnt exist: "
            + target_biome
        )
    else:
        ret = arules
        for b in arules:
            if b == src_biome:
                for _ in range(arules[b].count(target_biome) * scaling_factor):
                    ret[b].append(target_biome)
        return ret
    
def print_tileset(tileset):
    string = ""
    for c in tileset:
        string = string + "\033[0;32;40m" + c + "\033[0;0m" + ":\n"
        for x in tileset[c]:
            string = string + "\033[0;34;40m" + x + "\033[0;0m" + ":" + tileset[c][x] + "\n"
    return string

def print_rules(rules):
    string = ""
    for k in rules:
        string = string + "\033[0;32;40m" + k + "\033[0;0m" + ":\n"
        temp = []
        for b in rules[k]:
            if not b in temp:
                temp.append(b)
                string = string + b + "->" + str(rules[k].count(b)) + "\n"
    print(string)

def print_map(map):
    max_x = None
    max_y = None
    min_x = None
    min_y = None
    for k in map.chunks:
        if max_x == None or int(k[0]) > max_x:
            max_x = int(k[0])
        if min_x == None or int(k[0]) < min_x:
            min_x = int(k[0])
        if max_y == None or int(k[1]) > max_y:
            max_y = int(k[1])
        if min_y == None or int(k[1]) < min_y:
            min_y = int(k[1])
    strd = ""
    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            if list(map.chunks.keys()).count((x, y)) > 0:
                strd += map.chunks[(x, y)].display
            else:
                strd += "\033[0;30;47m \033[0;0m"
        if y > min_y - 1:
            strd += "\n"
    sys.stdout.write(strd)

def print_all(map):
    max_x = None
    max_y = None
    min_x = None
    min_y = None
    for k in map.locations:
        if max_x == None or int(k[0]) > max_x:
            max_x = int(k[0])
        if min_x == None or int(k[0]) < min_x:
            min_x = int(k[0])
        if max_y == None or int(k[1]) > max_y:
            max_y = int(k[1])
        if min_y == None or int(k[1]) < min_y:
            min_y = int(k[1])
    strd = ""
    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            if list(map.locations.keys()).count((x, y)) > 0:
                strd += map.locations[(x, y)].display()
            else:
                strd += "\033[0;30;47m \033[0;0m"
        if y > min_y - 1:
            strd += "\n"
    sys.stdout.write(strd)

def print_all_player(map, p):
    max_x = None
    max_y = None
    min_x = None
    min_y = None
    for k in map.locations:
        if max_x == None or int(k[0]) > max_x:
            max_x = int(k[0])
        if min_x == None or int(k[0]) < min_x:
            min_x = int(k[0])
        if max_y == None or int(k[1]) > max_y:
            max_y = int(k[1])
        if min_y == None or int(k[1]) < min_y:
            min_y = int(k[1])
    strd = ""
    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            if list(map.locations.keys()).count((x, y)) > 0:
                if p.x == x and p.y == y:
                    strd += p.symbol
                else:
                    strd += map.locations[(x, y)].display()
            else:
                strd += "\033[0;30;47m \033[0;0m"
        if y > min_y - 1:
            strd += "\n"
    sys.stdout.write(strd)

def find_coords_in_chunk(x, y, m):
    for xc,yc in m.chunks:
        if (x,y) in m.chunks[xc, yc].coords:
            return xc, yc
    return False

def find_closest_chunk(x, y, size):
    dist = (size - 1) // 2
    xt = 0
    yt = 0
    while True:
        if abs(xt*size - x) <= dist and abs(yt*size - y) <= dist:
            #print(str(x) + "," + str(y) + " is in chunk " + str(xt) + "," + str(yt))
            return xt, yt
        else:
            xt, yt = _enumerate_origin(0, 0, xt, yt)


#4,5
#5,5

# 1234