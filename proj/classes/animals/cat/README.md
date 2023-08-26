# class _Cat_


The class _Cat_ has the numbers of front and hind legs as parameters.<br>
(Both are 2 by default.)

The properties _clawnum_ and _pawnum_ are calculated based on the numbers of legs.<br>
(A standard cat has 2 · 5 + 2 · 4 = 18 claws and 2 + 2 = 4 paws.)

The gist of this code is, that the properties do not appear in the class definition of _Cat_.<br>
Instead they are in the class definition of _CatProperties_, which contains nothing else.<br>
This makes it possible to add properties with the script [_prop_maker_](../../../scripts/prop_maker).


* **cat**
  * [init](__init__.py): &nbsp; _Cat_ defined as child of _CatProperties_.
  * **properties**
    * [init](properties/__init__.py): &nbsp; _CatProperties_ contains the imports from subfolders.
    * **clawnum**
      * [init](properties/clawnum/__init__.py): &nbsp; calculate _clawnum_
      * [test](properties/clawnum/_test.py): &nbsp; check if _clawnum_ works
    * **pawnum**
      * [init](properties/pawnum/__init__.py): &nbsp; calculate _pawnum_
      * [test](properties/pawnum/_test.py): &nbsp; check if _pawnum_ works
    * **claws_per_paw** &nbsp; (depending on _clawnum_ and _pawnum_)
      * [init](properties/claws_per_paw/__init__.py): &nbsp; calculate _claws_per_paw_
      * [test](properties/claws_per_paw/_test.py): &nbsp; check if _claws_per_paw_ works
    * **whiskers** &nbsp; (raw property as added by _prop_maker_)
      * [init](properties/whiskers/__init__.py): &nbsp; dummy of _whiskers_
      * [test](properties/whiskers/_test.py): &nbsp; dummy test of _whiskers_
