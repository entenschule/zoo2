# create class _Dog_

The [function](functions.py) `create_class` will create the class [_Dog_](../../classes/animals/dog),
and `delete_class` will undo it.

The functions can be run like this:

```python
from proj.scripts.dummy_class.functions import create_class, delete_class


create_class()
delete_class()
```

The class works like this:

```python
from proj.classes.animals.dog import Dog


dog = Dog()  # standard dog with 4 legs
assert dog.sound == 'whoof'
assert dog.clawnum == 20

dog = Dog(3)  # dog with 3 legs
assert dog.clawnum == 15
```

## [test](_test.py)

The tests use `create_class` to create the _Dog_ class, and successfully assert it to work.

The second function `attr_fun` adds a second class attribute.<br>
The second test shows this to work as well.

This was done, to find out why the [_prop_ tests](../prop/test) fail.
But the basic approach is proven to work:<br>
The script changes the class file, then imports the class, and the changes have taken effect.
