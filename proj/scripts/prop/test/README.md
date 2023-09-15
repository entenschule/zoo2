# test creation and deletion of properties

[These are two tests](_test.py) of the function `create_or_delete_property` in [_function.py_](../function.py).<br>
The first test asserts, that a new property works after adding it.

The tests must be run with the `-m` switch, to add folder _proj_ to the path.<br>
The following command is to be run in the root folder _zoo2_:

```
python -m pytest proj/scripts/prop
```

**Both tests fail.** This is because the script somehow imports the _cat_ module in its old state.<br>
The explicit import in the test does not overwrite it. (See [question on Stackoverflow](https://stackoverflow.com/questions/77081775).)

(Compare [these passing tests](../../../classes/animals/cat/properties/_test.py), which do not involve the script.)

There are [extensive versions](_test_extensive.py) of the two tests,
which proof, that the files have indeed been changed as expected.


## log

Currently, the test permanently appends the [log file](../log.md),
but it does not test, if the logging works.<br>
Eventually that should be changed: It should be tested, but the test should leave not traces.
