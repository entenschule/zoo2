# create class _Dog_

This [function](functions.py) `class_fun` will create or delete the class [_Dog_](../../classes/animals/dog).

```python
from proj.classes.animals.dog import Dog


dog = Dog()
assert dog.sound == 'whoof'
```

## [test](_test.py)

The tests use `class_fun` to create the _Dog_ class, and successfully assert it to work.

The second function `attr_fun` adds a second class attribute.<br>
The second test shows this to work as well.

This was done, to find out why the [_prop_ tests](../prop/test) fail.
But the basic approach is proven to work:<br>
The script changes the class file, then imports the class, and the changes have taken effect.