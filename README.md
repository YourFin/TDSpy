# TDS.py

This software aims to provide a way of creating and manipulating Tile-Assembly systems in python 3, and exporting these objects to the `.tds` format used by the [ISU TAS](http://self-assembly.net/wiki/index.php?title=ISU_TAS) simulation software.

## Usage

This library creates three classes: `Tile`s, `Glue`s, and `TAS`'s. The `Tile` and `Glue` classes are written such that they can easily be made to fit a hierarchical structure with inherited traits.

### Glue

Constructor: `Glue(str label, int strength, optional Glue parent)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create a new Glue with label `label`, strength `strength`  

  

`create_child(str labelSuffix, optional int strength)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create a new Glue of name `{label}{labelSuffix}` as a child of `self`. Default strength is that of the parent.
	
