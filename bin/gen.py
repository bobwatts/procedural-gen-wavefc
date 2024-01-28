import sys
sys.path.insert(1, "src")
import functions
import map
sys.path.clear
sys.path.insert(1, "data")
import gen_rules


rules = gen_rules.rules

r = functions.scale_down_biome_rarity(rules, "edge mountains", 10)
b = functions.scale_biome_rarity(r, "mountains", 20)
c = functions.scale_specfic_biome(b, "edge mountains", "edge mountains", 20)
c = functions.scale_biome_rarity(c, "ocean", 5)
m = map.Map(c, gen_rules.loc_rules, gen_rules.biome_loc_rules, 5)
m.generate_new_map(10)
functions.print_map(m)
print("------------------------------")
functions.print_all(m)