    # def generate_chunk(self, chunk, x, y):
    #     d = (self.chunk_size-1)//2
    #     x = x*self.chunk_size
    #     y = y*self.chunk_size
    #     corners = {(x + d, y + d): 0, (x - d, y + d): 0, (x - d, y - d): 0, (x + d, y - d): 0}
    #     for xt, yt in list(corners.keys()):
    #         adj = [(xt + 1, yt), (xt, yt + 1), (xt - 1, yt), (xt, yt - 1)]
    #         for h in list(adj):
    #             if h in self.locations:
    #                 corners[xt,yt] += 1
    #     max = None
    #     max_val = None
    #     for i in corners:
    #         if max == None or corners[i] > max_val:
    #             max = i
    #             max_val = corners[i]
    #             quad = list(corners.keys()).index(i)+1
    #     xc = max[0]
    #     yc = max[1]
    #     for i in range(self.chunk_size*self.chunk_size):
    #         t = [(xc + 1, yc), (xc, yc + 1), (xc - 1, yc), (xc, yc - 1)]
    #         possible_loc = list(chunk.possible_locations)
    #         for c in t:
    #             if c in self.locations:
    #                 possible_loc = functions.set_intersect_weighted(
    #                     possible_loc, self.loc_rules[self.locations[c[0],c[1]].object]
    #                 )
    #         if len(possible_loc) == 0:
    #             self.locations[(xc, yc)] = loc.Loc("Err")
    #             print("\033[0;33;42merror, no possible locations\033[0;0m")
    #         else:
    #             n = [(xc + 1, yc), (xc - 1, yc), (xc, yc + 1), (xc, yc - 1)]
    #             done = False
    #             for xk, yk in n:
    #                 chunk_coords = [ (xc, yc) for xc in range(x-d, x+d+1) for yc in range(y-d,y+d+1)]
    #                 chunk_border = []
    #                 for xj, yj in chunk_coords:
    #                     #instead of long or statement, only recognize edge on side nearest to coords
    #                     if abs((x-d) - xj) <= (d//3) or abs((x+d) - xj) <= (d//3) or abs((y-d) - yj) <= (d//3) or abs((y+d) - yj) <= (d//3):
    #                         chunk_border.append((xj, yj))
    #                 # print(len(chunk_border))
    #                 if (xk, yk) in self.locations and self.locations[xk, yk].biome != chunk.biome and (xc, yc) in chunk_border:
    #                     test_arr = [0, 1, 1]
    #                     random.shuffle(test_arr)
    #                     if test_arr[0] == 0:
    #                         random.shuffle(possible_loc)
    #                         # print("Biome:" + str(chunk.biome) + "\npossible:" + str(possible_loc))
    #                         self.locations[(xc, yc)] = loc.Loc(chunk.biome, possible_loc[0])
    #                         done = True
    #                     else:
    #                         done = True
    #                         self.locations[(xc, yc)] = loc.Loc(self.locations[xk, yk].biome, "empty")
    #                     break
    #             if not done:
    #                 # print("Biome:" + str(chunk.biome) + "\npossible:" + str(possible_loc))
    #                 random.shuffle(possible_loc)
    #                 self.locations[(xc, yc)] = loc.Loc(chunk.biome, possible_loc[0])
    #         if i != self.chunk_size*self.chunk_size-1:
    #             xc, yc = functions._enumerate_corner(max[0], max[1], xc, yc, quad, self.chunk_size)