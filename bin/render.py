import os
import sys
sys.path.insert(1, "src")
import player
import map
import functions
sys.path.clear
sys.path.insert(1, "data")
import gen_rules


r = functions.scale_down_biome_rarity(gen_rules.rules, "edge mountains", 10)
b = functions.scale_biome_rarity(r, "mountains", 20)
c = functions.scale_specfic_biome(b, "edge mountains", "edge mountains", 20)
c = functions.scale_biome_rarity(c, "ocean", 5)
m = map.Map(c, gen_rules.loc_rules, gen_rules.biome_loc_rules, 7)
m.generate_new_map(10)
functions.print_map(m)
print("------------------------------")
functions.print_all(m)
print("------------------------------")

p = player.Player(0, 0, '\033[0;34;40m@\033[0;0m')

game = True
while game:
    os.system("clear")
    print("_________________")
    m.render_surroundings(p.x,p.y,3,8,p.symbol)   #make function for finding coords of chunk
    # m.render_surroundings(p.x,p.y,2,2,p.symbol)
    sys.stdout.write("(X,Y): " + str(p.x) + ", " + str(p.y) + "\nChunk (X,Y):" + str(functions.find_coords_in_chunk(p.x, p.y, m)) + "\n>>")
    ans = input().lower()
    if ans == "quit":
        game = False
    if ans == "n":
        p.move("n", m)
    elif ans == "s":
        p.move("s", m)
    elif ans == "e":
        p.move("e", m)
    elif ans == "w":
        p.move("w", m)
    elif ans == "debug":
        functions.print_all_player(m, p)
        ans = input().lower()