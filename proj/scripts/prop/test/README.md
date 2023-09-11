# test creation and deletion of properties

This will test if the function `create_or_delete_property` in [_function.py_](../function.py) works.<br>
That is the case, if a new property works after adding it,<br>
and if no traces remain after removing it.<br>


The tests must be run with the `-m` switch, to add folder _proj_ to the path.

```
python -m pytest proj/scripts/prop
```

Both tests fail. (Compare [these passing tests](../../../classes/animals/cat/properties/_test.py).)<br>
They also show, that the update of 
[_names_](../../../classes/animals/cat/properties/names.py) 
and [_CatProperties_](../../../classes/animals/cat/properties/__init__.py)
has worked,<br>
and that the property folder has been created.<br>
But the class instance does not reflect the change<br>(although the class is imported after running the script).


## log

Currently, the test permanently appends the [log file](../log.md),
but it does not test, if the logging works.<br>
Eventually that should be changed: It should be tested, but the test should leave not traces.
