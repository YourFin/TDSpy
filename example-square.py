#!/usr/bin/env python3

from TDS import *
from sys import argv

# Simple example that takes a number from the
# command line and creates a tileset to produce a square
# of that size

# Usage: ./example-square 20

# Handle command line input
if argv.__len__() == 1:
    square_len = 10
elif argv.__len__() == 2:
    square_len = int(argv[1])
else:
    print("Invalid command line arguments")
    exit(1)

# Create TAS
tas = TAS()

# "Constants"
dead_glue = Glue("", 0)
blank_tile = Tile("Fill Tile", [255, 255, 255])

# Create side glues
glue_parent = Glue("Side", 2)
glues = []

for index in range(square_len):
    glues.append(glue_parent.create_child("_" + str(index)))


seed_tile = Tile.create_compass("Seed", [255, 0, 0],
                                northGlue=glues[0],
                                eastGlue=glues[0],
                                southGlue=dead_glue,
                                westGlue=dead_glue)

# Create side and bottom tiles
side_tiles = []
bottom_tiles = []

for index in range(1, square_len):
    side_tiles.append(seed_tile.create_child("-side-" + str(index),
                                             northGlue=blank_glue,
                                             eastGlue=glues[index],
                                             westGlue=glues[index - 1]))
    # Bottom tiles are just side tiles but rotated clockwise 90
    # and flipped, so create it as such
    bottom_tiles.append(side_tiles[index - 1].rotate(1).vert_flip(inPlace=False))

# Add tiles to TAS
for tile in side_tiles + bottom_tiles + [seed_tile]:
    tas.addTile(tile)

tas.addTile(blank_tile, "fill")

# Write out the resultant assembly to a file
tas.printToFile("example-square.tds")
