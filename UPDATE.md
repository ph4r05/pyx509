## Migrations

Migration from `pyasn-0.2.3` to `pyasn1-0.3.3` required some code changes:

 - Cannot use `._value` directly. Object model has been overhauled and this is not allowed anymore. New models
 support new protocols (`dict`, `len`, `__getitem__` ...) and thus the object can be usually used directly.

 ```
 # change
 result = value._value

 # to
 result = value
 ```



