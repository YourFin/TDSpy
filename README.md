# TDS.py

This software aims to provide a way of creating and manipulating Tile-Assembly systems in python 3, and exporting these objects to the `.tds` format used by the [ISU TAS](http://self-assembly.net/wiki/index.php?title=ISU_TAS) simulation software.

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

`Tile create_child(optional str tilenameSuffix, optional list(int) colorDif, optional Glue northGlue, optional Glue eastGlue, optional Glue southGlue, optional Glue westGlue)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create a new `Tile` of name `{tilename}{tilenameSuffix}`as a child of `self`. `colorDif` is added to the parent's color, and the glues defualt to the parent's.  

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
