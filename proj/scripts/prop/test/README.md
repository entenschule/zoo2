# test

This will test if the function `prop_fun` in [_function.py_](../function.py) works.<br>
That is the case, if a new property works after adding it,<br>
and if no traces remain after removing it.


The tests must be run with the `-m` switch, to add folder _proj_ to the path.

```
python -m pytest
python -m pytest proj/scripts
```

The fixture `prop_foo` in [_conftest.py_](conftest.py) creates the property _foo_.

This works, **but the test fails anyway**:<br>
`AttributeError: 'Cat' object has no attribute 'foo'`

Eventually the fixture should also delete the property when the test is finished.<br>
Currently that has to be done manually:

```
python -m proj.scripts.prop delete animals.cat foo
```
