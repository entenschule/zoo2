# test creation and deletion of properties

This will test if the function `prop_fun` in [_function.py_](../function.py) works.<br>
That is the case, if a new property works after adding it,<br>
and if no traces remain after removing it.<br>


The tests must be run with the `-m` switch, to add folder _proj_ to the path.

```
python -m pytest proj/scripts
```

## create

The fixture `prop_foo` in [_conftest.py_](conftest.py) creates the property _foo_.

This works, **but the test fails anyway**:<br>
`AttributeError: 'Cat' object has no attribute 'foo'`


## delete

Eventually the fixture should also delete the property, when the test is finished.<br>
Currently that has to be done manually:

```
python -m proj.scripts.prop delete animals.cat foo
```


## log

Currently, the test permanently appends the [log file](../log.md),
but it does not test, if the logging works.<br>
Eventually that should be changed: It should be tested, but the test should leave not traces.
