# prop_maker

This function adds a property to a class.

Example command to be run in _zoo_ folder:<br>
`python proj/scripts/prop_maker animals.cat whiskers`

This will create the folder [_classes/animals/cat/properties/whiskers_](../../classes/animals/cat/properties/whiskers)
and the files in it, especially the [init file](../../classes/animals/cat/properties/whiskers/__init__.py).<br>
It will also append [_prop_log.md_](../prop_log.md), which then contains a link to the created folder.

The first argument is the path to the class folder,
and the second one is the name of the property to be added.

This is assumed:
* The class is nested in [_proj/classes_](../../../proj/classes).
* It has a _properties_ folder like [cat/properties](../../classes/animals/cat/properties).
* In it is an init file like [this](../../classes/animals/cat/properties/__init__.py)
and a _names.py_ like [this](../../classes/animals/cat/properties/names.py).
