# create and delete properties

These scripts add and remove properties of a class.


## create

```
python -m proj.scripts.prop create animals.cat whiskers
```

The example command shown above is to be run in the root folder (_zoo2_),<br>
and will do the following:

* create folder [_animals/cat/properties/whiskers_](../../classes/animals/cat/properties/whiskers)
with [init](../../classes/animals/cat/properties/whiskers/__init__.py)
and [test](../../classes/animals/cat/properties/whiskers/_test.py) file
* append [imports](../../classes/animals/cat/properties/__init__.py)
and [names](../../classes/animals/cat/properties/names.py) of properties
* append [_log.md_](log.md) (which then contains a link to the created folder)

The first argument is the path to the class folder,
and the second one is the name of the property to be added.

These assumptions are made:

* The class is nested in [_proj/classes_](../../../proj/classes).
* It has a _properties_ folder (like [_cat/properties_](../../classes/animals/cat/properties)).
* That contains an init file and _names.py_ (like [this](../../classes/animals/cat/properties/__init__.py)
and [that](../../classes/animals/cat/properties/names.py)).
* (Also that the [log file](log.md) exists.)

## delete

```
python -m proj.scripts.prop delete animals.cat tail
```

The example command shown above is to be run in the root folder (_zoo2_),<br>
and will do the following:

* remove folder _animals/cat/properties/tail_ and its contents
* remove the corresponding entry from imports and names
* append the log file

----

In the [main](__main__.py) file the parameters are passed to `prop_fun` in [_function.py_](function.py).<br>
That can also be called directly:

```python
from proj.scripts.prop.function import prop_fun


prop_fun('create', 'animals.cat', 'ears')
prop_fun('delete', 'animals.cat', 'ears')
```
