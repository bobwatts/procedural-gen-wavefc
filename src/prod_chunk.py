import loc
import random
import functions
import sys
import map
sys.path.append("data")
import gen_rules

class Chunk:
    def __init__(self, biome, biome_loc_rules, coords):
        self.biome = biome
        # self.dim = 5
        # self.rules = gen_rules.loc_rules
        biome_loc_rules = biome_loc_rules
        self.coords = []
        if biome == "ocean":
            self.display = gen_rules.tileset["biomes"]["ocean"]
            self.possible_locations = biome_loc_rules[biome]
        elif biome == "beach":
            self.display = gen_rules.tileset["biomes"]["beach"]
            self.possible_locations = biome_loc_rules[biome]
        elif biome == "plains":
            self.display = gen_rules.tileset["biomes"]["plains"]
            self.possible_locations = biome_loc_rules[biome]
        elif biome == "sparse forest":
            self.display = gen_rules.tileset["biomes"]["sparse forest"]
            self.possible_locations = biome_loc_rules[biome]
        elif biome == "deep forest":
            self.display = gen_rules.tileset["biomes"]["deep forest"]
            self.possible_locations = biome_loc_rules[biome]
        elif biome == "edge ocean":
            self.display = gen_rules.tileset["biomes"]["ocean"]
            self.possible_locations = biome_loc_rules[biome]
        elif biome == "edge beach":
            self.display = gen_rules.tileset["biomes"]["beach"]
            self.possible_locations = biome_loc_rules[biome]
        elif biome == "edge plains":
            self.display = gen_rules.tileset["biomes"]["plains"]
            self.possible_locations = biome_loc_rules[biome]
        elif biome == "edge sparse forest":
            self.display = gen_rules.tileset["biomes"]["sparse forest"]
            self.possible_locations = biome_loc_rules[biome]
        elif biome == "edge deep forest":
            self.display = gen_rules.tileset["biomes"]["deep forest"]
            self.possible_locations = biome_loc_rules[biome]
        elif biome == "edge mountains":
            self.display = gen_rules.tileset["biomes"]["edge mountains"]
            self.possible_locations = biome_loc_rules[biome]
        elif biome == "mountains":
            self.display = gen_rules.tileset["biomes"]["mountains"]
            self.possible_locations = biome_loc_rules[biome]
        else:
            self.display = gen_rules.tileset["biomes"]["error"]
            self.possible_locations = []