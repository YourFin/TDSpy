#!/usr/bin/env python3

class Glue:
    """A TAS side glue"""
    def __init__(self, label, strength, parent=None):
        if isinstance(strength, int) and isinstance(label, str):
            self.strength = strength
            self.label = label
            self.children = []
        else:
            raise ValueError('Invalid input for Glue')

        if parent is None or isinstance(parent, Glue):
            self.parent = parent
        else:
            raise ValueError('parent needs to be of type glue')

    @classmethod
    def create_child(parent, labelSuffix, strength=None):
        if isinstance(parent, Glue) and isinstance(labelSuffix, str):
            parent.children += self
            if strength is None:
                return Glue(parent.label + labelSuffix, parent.strength, parent)
            elif isinstance(strength, int):
                return Glue(parent.label + labelSuffix, strength, parent)
            else:
                raise ValueError('Strength must be an integer.')
        else:
            raise ValueError('Invalid input for Glue constructor')
            
    blank_glue = Glue(1, "")

    def __str__(self):
        return "{0}: {1}".format(label, strength)
            
class Tile:
    """A pythonic representation of TAS tiles"""
    def __init__(self, tilename, color=[255, 255, 255], northGlue=Glue.blank_glue, eastGlue=Glue.blank_glue, southGlue=Glue.blank_glue, westGlue=Glue.blank_glue):
        self.glues = [northGlue, eastGlue, southGlue, westGlue]
        self.tilename = tilename
        self.color = color

    def __init__(self, tilename, color=[255, 255, 255], glues=([Glue.blank_glue] * 4)):
        self.glues = glues
        self.tilename = tilename
        self.color = color

    def __init__(self, parent, tilename_suffix="", color_dif=[0,0,0]):
        self.glues = parent.glues
        self.color = [(x + y) % 255 for x, y in zip(parent.color, color)]
        self.tilename = parent.tilename + tilename_suffix

class TAS:
    def __init__(self):
        self.tiles = {}

    def addTile(self, tile, label=None):
        """Add a tile to the TAS. Labels must be unique. Defaults to tile name"""
        if label is None:
            label = tile.tilename
        if label in self.tiles:
            raise ValueError('Tile labes must be unique')
        self.tiles[label] = tile

    tilestring = textwrap.dedent("""\
    TILENAME {tile_name}
    LABEL {label}
    NORTHBIND {north_bind_strength}
    EASTBIND {east_bind_strength}
    SOUTHBIND (south_bind_strength)
    WESTBIND {west_bind_strength}
    NORTHLABEL {north_label}
    EASTLABEL {east_label)}
    SOUTHLABEL {south_label}
    WESTLABEL {west_label}
    TILECOLOR rgb({color_red}, {color_green}, {color_blue})
    CREATE
    
    
    """)

    def printTiles(self):
        """Print out the tileset in a tds friendly format"""
        output = ""
        for label, tile in self.tiles.items():
            output += tiletext.format(
                tilename=tile.tilename, label=label,
                north_label=tile.glues[0].label, north_glue_strength=tile.glues[0].strength,
                east_label=tile.glues[1].label,  east_glue_strength=tile.glues[1].strength,
                south_label=tile.glues[2].label, south_glue_strength=tile.glues[2].strength,
                west_label=tile.glues[3].label,  west_glue_strength=tile.glues[3].strength,
                color_red=tile.color[0], color_green=tile.color[1], color_blue=tile.color[2]
            )
        return output

    def printToFile(self, path):
        with open(path, 'w') as ff:
            ff.write(self.printTiles())
            print("TAS written to {0}.".format(path))
