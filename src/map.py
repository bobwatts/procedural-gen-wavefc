import prod_chunk
import sys
import random
import functions
import loc
sys.path.append("data")


class Map:
    def __init__(self, rules, loc_rules, biome_loc_rules, chunk_size, chunks={}, locations={}):
        self.rules = rules
        self.chunk_size = chunk_size # must be odd
        self.chunks = chunks
        self.locations = locations
        self.loc_rules = loc_rules
        self.biome_loc_rules = biome_loc_rules

    # def generate_new_map(self, size):
    #     total_chunks = size * size
    #     x, y = 0, 0
    #     for i in range(total_chunks):
    #         t = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
    #         possible_biomes = list(self.rules)
    #         for c in t:
    #             if c in self.chunks:
    #                 possible_biomes = functions.set_intersect_weighted(
    #                     possible_biomes, self.rules[self.chunks[c].biome]
    #                 )
    #         if len(possible_biomes) == 0:
    #             print("Chunk problem")
    #             self.chunks[(x, y)] = prod_chunk.Chunk("Err", self.biome_loc_rules)
    #             self.generate_chunk(self.chunks[(x, y)], x, y)
    #         else:
    #             random.shuffle(possible_biomes)
    #             self.chunks[(x, y)] = prod_chunk.Chunk(possible_biomes[0], self.biome_loc_rules)
    #             # print("Generating chunk:" + str(x) + ", " + str(y))
    #             self.generate_chunk(self.chunks[(x, y)], x, y)
    #         x, y = functions._enumerate_origin(0, 0, x, y)
    def make_chunk(self, x, y):
        t = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
        possible_biomes = list(self.rules)
        for c in t:
            if c in self.chunks:
                possible_biomes = functions.set_intersect_weighted(
                    possible_biomes, self.rules[self.chunks[c].biome]
                )
        if len(possible_biomes) == 0:
            print("Chunk problem")
            self.chunks[(x, y)] = prod_chunk.Chunk("Err", self.biome_loc_rules, [])
            self.generate_chunk(self.chunks[(x, y)], x, y)
        else:
            random.shuffle(possible_biomes)
            self.chunks[(x, y)] = prod_chunk.Chunk(possible_biomes[0], self.biome_loc_rules, [])
            # print("Generating chunk:" + str(x) + ", " + str(y))
            self.generate_chunk(self.chunks[(x, y)], x, y)

    def generate_new_map(self, size):
        total_chunks = size * size
        x, y = 0, 0
        for i in range(total_chunks):
            self.make_chunk(x, y)
            x, y = functions._enumerate_origin(0, 0, x, y)

    def generate_chunk(self, chunk, x, y):
        d = (self.chunk_size-1)//2
        x = x*self.chunk_size
        y = y*self.chunk_size
        chunk.coords = [ (xc, yc) for xc in range(x-d, x+d+1) for yc in range(y-d,y+d+1)]        
        corners = {(x + d, y + d): 0, (x - d, y + d): 0, (x - d, y - d): 0, (x + d, y - d): 0}
        for xt, yt in list(corners.keys()):
            adj = [(xt + 1, yt), (xt, yt + 1), (xt - 1, yt), (xt, yt - 1)]
            for h in list(adj):
                if h in self.locations:
                    corners[xt,yt] += 1
        max = None
        max_val = None
        for i in corners:
            if max == None or corners[i] > max_val:
                max = i
                max_val = corners[i]
                quad = list(corners.keys()).index(i)+1
        xc = max[0]
        yc = max[1]
        for i in range(self.chunk_size*self.chunk_size):
            t = [(xc + 1, yc), (xc, yc + 1), (xc - 1, yc), (xc, yc - 1)]
            possible_loc = list(chunk.possible_locations)
            for c in t:
                if c in self.locations:
                    possible_loc = functions.set_intersect_weighted(
                        possible_loc, self.loc_rules[self.locations[c[0],c[1]].object]
                    )
            if len(possible_loc) == 0:
                self.locations[(xc, yc)] = loc.Loc("Err")
                print("\033[0;33;42merror, no possible locations\033[0;0m")
            else:
                n = [(xc + 1, yc), (xc - 1, yc), (xc, yc + 1), (xc, yc - 1)]
                done = False
                for xk, yk in n:
                    chunk_coords = [ (xc, yc) for xc in range(x-d, x+d+1) for yc in range(y-d,y+d+1)]
                    chunk_border = []
                    for xj, yj in chunk_coords:
                        #instead of long or statement, only recognize edge on side nearest to coords
                        if abs((x-d) - xj) <= (d//3) or abs((x+d) - xj) <= (d//3) or abs((y-d) - yj) <= (d//3) or abs((y+d) - yj) <= (d//3):
                            chunk_border.append((xj, yj))
                    # print(len(chunk_border))
                    if (xk, yk) in self.locations and self.locations[xk, yk].biome != chunk.biome and (xc, yc) in chunk_border:
                        test_arr = [0, 1, 1]
                        random.shuffle(test_arr)
                        if test_arr[0] == 0:
                            random.shuffle(possible_loc)
                            # print("Biome:" + str(chunk.biome) + "\npossible:" + str(possible_loc))
                            self.locations[(xc, yc)] = loc.Loc(chunk.biome, possible_loc[0])
                            done = True
                        else:
                            done = True
                            self.locations[(xc, yc)] = loc.Loc(self.locations[xk, yk].biome, "empty")
                        break
                if not done:
                    # print("Biome:" + str(chunk.biome) + "\npossible:" + str(possible_loc))
                    random.shuffle(possible_loc)
                    self.locations[(xc, yc)] = loc.Loc(chunk.biome, possible_loc[0])
            if i != self.chunk_size*self.chunk_size-1:
                xc, yc = functions._enumerate_corner(max[0], max[1], xc, yc, quad, self.chunk_size)

    def render_surroundings(self, x, y, vert_edge, hori_edge, player_symbol):
        left_x = x - hori_edge
        top_y = y + vert_edge
        right_x = x + hori_edge
        bot_y = y - vert_edge
        strd = ""
        for yi in range(top_y, bot_y-1, -1):
            for xi in range(left_x, right_x+1):
                if yi == y and xi == x:
                    strd += player_symbol
                else:
                    if list(self.locations.keys()).count((xi,yi)) > 0:
                        strd += self.locations[(xi,yi)].display()
                    else:
                        xn, yn = functions.find_closest_chunk(xi, yi, self.chunk_size)
                        self.make_chunk(xn, yn)
                        #print("Generating chunk:" + str(xn) + ", " + str(yn))
                        # d = (self.chunk_size-1)//2
                        # x = x*self.chunk_size
                        # y = y*self.chunk_size
                        # chunk_coords = [ (xc, yc) for xc in range(x-d, x+d+1) for yc in range(y-d,y+d+1)]
                        #print("Containing coords:" + str(self.chunks[xn, yn].coords))
                        # print(((xi // self.chunk_size), (yi // self.chunk_size)) in self.chunks)
                        self.generate_chunk(self.chunks[xn, yn], xn, yn)
                        #print(xn, yn)
                        strd += self.locations[(xi,yi)].display()
            if yi >= bot_y:
                strd += "\n"
        sys.stdout.write(strd)