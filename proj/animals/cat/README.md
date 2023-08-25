# class _Cat_


The class `Cat` has the numbers of front and hind legs as parameters.<br>
Both are 2 by default.

The property `clawnum` is calculated based on the numbers of legs.<br>
For a standard cat it is 2 &middot; 5 + 2 &middot; 4 = 18.

* **cat**
  * [init](__init__.py): &nbsp; _Cat_ defined as child of _CatProperties_.
  * **properties**
    * [init](properties/__init__.py): &nbsp; _CatProperties_ wraps the imports from subfolders.
    * **clawnum**
      * [init](properties/clawnum/__init__.py): &nbsp; calculate property
      * [test](properties/clawnum/_test.py): &nbsp; check if property works
