# TDS.py

This software aims to provide a way of creating and manipulating Tile-Assembly systems in python 3, and exporting these objects to the `.tds` format used by the [ISU TAS](http://self-assembly.net/wiki/index.php?title=ISU_TAS) simulation software.

## Usage

This library creates three classes: `Tile`s, `Glue`s, and `TAS`'s. The `Tile` and `Glue` classes are written such that they can easily be made to fit a hierarchical structure with inherited traits.

### Glue

#### Functions:

Constructor: `Glue(str label, int strength, optional Glue parent)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create a new Glue with label `label`, strength `strength`  
`create_child(str labelSuffix, optional int strength)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create a new Glue of name `{label}{labelSuffix}` as a child of `self`. Default strength is that of the parent.
	
### Tile

#### Functions:

Constructor: `Tile(str tilename, optional list(int) color, optional list(Glue) glues, optional Tile parent)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create a new `Tile` with name `tilename`. Defaults to white, blank glues, and no parent.

`Tile create_compass(str tilename, optional list(int) color, optional Glue northGlue, optional Glue eastGlue, optional Glue southGlue, optional Glue westGlue)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create a new `Tile` with name `tilename` using names instead of the list format.

`Tile create_child(optional str tilenameSuffix, optional list(int) colorDif, optional Glue northGlue, optional Glue eastGlue, optional Glue southGlue, optional Glue westGlue)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create a new `Tile` as a child of the current
