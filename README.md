# TDS.py

This software aims to provide a way of creating and manipulating Tile-Assembly systems in python 3, and exporting these objects to the `.tds` format used by the [ISU TAS](http://self-assembly.net/wiki/index.php?title=ISU_TAS) simulation software.

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [TDS.py](#tdspy)
    - [Usage](#usage)
    - [Documentation](#documentation)
        - [Glue Class](#glue-class)
            - [Variables:](#variables)
            - [Functions:](#functions)
        - [Tile Class](#tile-class)
            - [Variables:](#variables-1)
            - [Functions:](#functions-1)
        - [TAS Class](#tas-class)
            - [Variables:](#variables-2)
            - [Functions:](#functions-2)
    - [Licence](#licence)

<!-- markdown-toc end -->

## Usage

This library creates three classes: `Tile`s, `Glue`s, and `TAS`'s. The `Tile` and `Glue` classes are written such that they can easily be made to fit a hierarchical structure with inherited traits. Pull requests welcome :)

## Documentation

### Glue Class

#### Variables:

`strength`: The `int` strength of this glue

`label`: The `str` name of this glue

`parent`: The `Glue` that this glue is derived from

`children`: The `list(Glue)` of all children of this glue.

#### Functions:

Constructor: `Glue(str label, int strength, optional Glue parent)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create a new Glue with label `label`, strength `strength`

`create_child(str labelSuffix, optional int strength)`  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create a new Glue of name `{label}{labelSuffix}` as a child of `self`. Default strength is that of the parent.
	
### Tile Class
#### Variables:

`glues`: A `list(Glue)` that contains the glues on the side of the tile. N:0, E:1, S:2, W:4.

`tilename`: The color of the tile in RGB format, as a list of integers.

`parent`: The `Tile` which this tile is defined relative to. 

`children`: A `list(tile)` with all tiles defined relative to this tile

#### Functions:

Constructor: `Tile(str tilename, optional list(int) color, optional list(Glue) glues, optional Tile parent)`  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create a new `Tile` with name `tilename`. Defaults to white, blank glues, and no parent.

`Tile create_compass(str tilename, optional list(int) color, optional Glue northGlue, optional Glue eastGlue, optional Glue southGlue, optional Glue westGlue)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create a new `Tile` with name `tilename` using names instead of the list format.

`Tile create_func(str tilename, function(a,a)->(a,a) func, list(a) horizInputs, optional list(a) vertInputs, optional list(int) color)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create a list of tiles based on a given function. This method iterates through each combination horizontal and vertical inputs (using the same set for both if vertInputs is omitted), calls func(horiz, vert), and creates a tile (with all glues of strength 1) such that the inputs are fed through the west and south sides and the outputs are fed through the north and east sides. The function must return a tuple containing the horizontal and vertical output in that order. If other orientations, colorings, etc. are required, the tiles can be modified after this method is called.

`Tile create_child(optional str tilenameSuffix, optional list(int) colorDif, optional Glue northGlue, optional Glue eastGlue, optional Glue southGlue, optional Glue westGlue, optional list(Glue) glues)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create a new `Tile` of name `{tilename}{tilenameSuffix}`as a child of `self`. `colorDif` is added to the parent's color, and the glues defualt to the parent's.  

`rotate(int rotation, optional str tilenameSuffix, optional list(int) colorDif)`:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create a new `Tile` that is a rotation of self 90*`rotation` degress clockwise. Default name is `{self.tilename}-rot{rotation}`.

`Tile horiz_flip(bool inPlace=True)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Modify the current tile to flip it horizontally. If `inPlace` is false, return a new `Tile` instead of modifying the current one.

`Tile vert_flip(bool inPlace=True)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Modify the current tile to flip it vertically. If `inPlace` is false, return a new `Tile` instead of modifying the current one.

### TAS Class
The `TAS` class is a subclass of the built-in `dict` class, and as such any operation that can be preformed on a dict can be preformed on a `TAS`. Keys to the dict are the labels in the ISU TAS software, as they must be unique in any given tileset.

#### Variables:
`tilestring`: The massive string used to convert to the `.tds` format.

#### Functions:

`void addTile(Tile tile, optional str label)`: A simple wrap around the dictionary add function that enforces adding uniquely labeled tiles, and provides a default label in the tile name.

`str printTiles()`: Dumps the `.tds` representation of the tileset.

`void printToFile(str path)`: Writes the tileset to the file at path. Overwrites, not appends


## Licence
Mit

© 2017 Patrick Nuckolls
