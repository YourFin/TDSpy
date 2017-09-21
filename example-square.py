#!/usr/bin/env python3

from TDS import *
from sys import argv

# Simple example that takes a number from the
# command line and creates a tileset to produce a square
# of that size

# Usage: ./example-square 20

if argv.__len__() == 1:
    square_len = 10
elif argv.__len__() == 2:
    square_len = int(argv[1])
else:
    print("Invalid command line arguments")
    exit(1)

tas = TAS()

side_glue_parent = Glue("Side", 2)
dead_glue = Glue("", 0)
side_glues = []

for index in range(square_len):
    side_glues.append(side_glue_parent.create_child("_" + str(index)))

seed_tile = Tile.create_compass("Seed", [255, 0, 0],
                                northGlue=side_glues[0],
                                eastGlue=side_glues[0],
                                southGlue=dead_glue,
                                westGlue=dead_glue)

blank_tile = Tile("Fill Tile", [255, 255, 255])
side_tiles = []
bottom_tiles = []

for index in range(1, square_len):
    side_tiles.append(seed_tile.create_child("-side-" + str(index),
                                             northGlue=blank_glue,
                                             eastGlue=side_glues[index],
                                             westGlue=side_glues[index - 1]))
    bottom_tiles.append(side_tiles[index - 1].rotate(1).vert_flip(inPlace=False))

for tile in side_tiles + bottom_tiles + [seed_tile]:
    tas.addTile(tile)

tas.addTile(blank_tile, "fill")

tas.printToFile("example-square.tds")
