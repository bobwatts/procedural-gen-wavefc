import sys
sys.path.insert(1, "src")
import functions
sys.path.clear
sys.path.insert(1, "data")
import gen_rules

print(functions.print_tileset(gen_rules.tileset))