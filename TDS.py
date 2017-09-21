#!/usr/bin/env python3

import textwrap
import copy

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

    def create_child(self, labelSuffix, strength=None):
        ret = None
        if isinstance(labelSuffix, str):
            if strength is None:
                ret = Glue(self.label + labelSuffix, self.strength, self)
            elif isinstance(strength, int):
                ret = Glue(self.label + labelSuffix, strength, self)
            else:
                raise ValueError('Strength must be an integer.')
        else:
            raise ValueError('Invalid input for Glue constructor')

        self.children.append(ret)
        return ret

    def __str__(self):
        return ("Glue \"{0}\": {1}".format(self.label, self.strength))

    def __repr__(self):
        return "<" + self.__str__() + ">"
            
blank_glue = Glue("", 1)

class Tile:
    """A pythonic representation of TAS tiles"""

    def __init__(self, tilename, color=[255, 255, 255], glues=([blank_glue] * 4), parent=None):
        self.glues = glues
        self.tilename = tilename
        self.color = color
        self.parent = parent
        self.children = []

    @classmethod
    def create_compass(cls, tilename, color=[255, 255, 255], northGlue=blank_glue, eastGlue=blank_glue, southGlue=blank_glue, westGlue=blank_glue):
        return cls(tilename, color, [northGlue, eastGlue, southGlue, westGlue])

    def create_child(self, tilenameSuffix="", colorDif=[0,0,0], northGlue=None, eastGlue=None, southGlue=None, westGlue=None, glues=[None, None, None, None]):
        outglues = copy.copy(self.glues)
        if glues.__len__() > 4:
            raise ValueError("glues is too long")

        for index, glue in enumerate(glues):
            if glue is not None and isinstance(glue, Glue):
                outglues[index] = glue
        for index, glue in enumerate([northGlue, eastGlue, southGlue, westGlue]):
            if glue is not None and isinstance(glue, Glue):
                outglues[index] = glue

        ret = Tile(self.tilename + tilenameSuffix,
                    [(x + y) % 256 for x, y in zip(self.color, colorDif)],
                    outglues,
                    self)

        self.children.append(ret)
        return ret

    def rotate(self, rotation, tilenameSuffix=None, colorDif=[0,0,0]):
        if tilenameSuffix is None:
            tilenameSuffix = "-rot" + str(rotation)

        return self.create_child(tilenameSuffix, colorDif,
                                 glues=[self.glues[(x - rotation) % 4]
                                        for x in range(4)])


    def __str__(self):
        return "{0}: "

class TAS(dict):
    def __init__(self):
        super()

    def addTile(self, tile, label=None):
        """Add a tile to the TAS. Labels must be unique. Defaults to tile name"""
        if label is None:
            label = tile.tilename
        if label in self:
            raise ValueError('Tile labes must be unique')
        self.__setitem__(label, tile)

    tilestring = textwrap.dedent("""\
    TILENAME {tile_name}
    LABEL {label}
    NORTHBIND {north_glue_strength}
    EASTBIND {east_glue_strength}
    SOUTHBIND {south_glue_strength}
    WESTBIND {west_glue_strength}
    NORTHLABEL {north_label}
    EASTLABEL {east_label}
    SOUTHLABEL {south_label}
    WESTLABEL {west_label}
    TILECOLOR rgb({color_red}, {color_green}, {color_blue})
    CREATE
    
    
    """)

    def printTiles(self):
        """Print out the tileset in a tds friendly format"""
        output = ""
        for label, tile in zip(self.keys(), self.values()):
            output += TAS.tilestring.format(
                tile_name=tile.tilename, label=label,
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
