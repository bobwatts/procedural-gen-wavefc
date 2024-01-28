import sys
sys.path.append("data")
import gen_rules

class Loc:
    def __init__(self, biome, object="empty"):
        self.biome = biome
        if biome == "ocean":
            self.background = gen_rules.tileset["backgrounds"]["ocean"]
        elif biome == "beach":
            self.background = gen_rules.tileset["backgrounds"]["beach"]
        elif biome == "plains":
            self.background = gen_rules.tileset["backgrounds"]["plains"]
        elif biome == "sparse forest":
            self.background = gen_rules.tileset["backgrounds"]["sparse forest"]
        elif biome == "deep forest":
            self.background = gen_rules.tileset["backgrounds"]["deep forest"]
        elif biome == "edge ocean":
            self.background = gen_rules.tileset["backgrounds"]["ocean"]
        elif biome == "edge beach":
            self.background = gen_rules.tileset["backgrounds"]["beach"]
        elif biome == "edge plains":
            self.background = gen_rules.tileset["backgrounds"]["plains"]
        elif biome == "edge sparse forest":
            self.background = gen_rules.tileset["backgrounds"]["sparse forest"]
        elif biome == "edge deep forest":
            self.background = gen_rules.tileset["backgrounds"]["deep forest"]
        elif biome == "edge mountains":
            self.background = gen_rules.tileset["backgrounds"]["edge mountains"]
        elif biome == "mountains":
            self.background = gen_rules.tileset["backgrounds"]["mountains"]
        else:
            print("ERROR")
            self.background = gen_rules.tileset["backgrounds"]["error"]
        self.object = object
        if object != "empty":
            self.object_display = gen_rules.tileset["location"][object]

    def display(self):
        if self.object == None or self.object == "empty":
            return self.background#"\033[0;31;41mO\033[0;0m"
        else:
            return self.object_display
