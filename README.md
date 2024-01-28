# procedural-gen-wavefc

Initial Commit. Worked on this algorithm during the Summer of 2023 to act as
a world generator for games. It is based off of a wave function collapse
algorithm for the (pseudo) random generation of terrain. Given a ruleset, 
it can create a world with multiple biomes that are arranged in a grid of
squares called "chunks". These chunks are then filled with "locations" which
make up the actual map.

In order to get the desired effect, the ruleset can (and should) be finetuned
depending on the context of its use and intended size of the map.

Moving forward:
 - This code can be refined/optimized further
 - Create a protocol that ensures no biome (group of chunks) is too common
 or is too big and force a biome switch (so it is not necessary to tune as much)