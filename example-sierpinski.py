#!/usr/bin/env python3

from TDS import *

# Create TAS
tas = TAS()

# Create glues
dead_glue = Glue("", 0)
seed_glue = Glue("seed", 2)

# Create seed tiles
seed_tile = Tile("Seed", [255, 0, 0], [seed_glue, seed_glue, dead_glue, dead_glue])
seed_wframe = Tile("wframe", [255, 0, 0], [seed_glue, Glue("fill-1", 1), seed_glue, dead_glue])
seed_sframe = seed_wframe.rotate(-1)
tas.addTile(seed_tile)
tas.addTile(seed_wframe)
tas.addTile(seed_sframe)

# Create center tiles
def xor(horiz, vert):
    return horiz^vert, horiz^vert

fill_tiles = Tile.create_func("fill", xor, [0,1])
for tile in fill_tiles:
    if tile.glues[0].label == "fill-1": 
        tile.color = [255,0,0]
    tas.addTile(tile)

tas.printToFile("example-sierpinski.tds")
