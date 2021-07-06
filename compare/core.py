from functools import partial
from collections import defaultdict
import logging
import types

ORDERS = defaultdict(int)
MAX_DEPTH = 2


class Value:

    def __add__(self, other):
        print('add...')
        return 0.0


class Comp:

    def __init__(self,  *objs, recursion_level=1, **kwobjs) -> None:
        self._recursion_level = recursion_level
        self._objects = dict()
        # TODO: verify object type are same? or we just duck typing... and throw runtime exception..
        for o in objs:
            cl = o.__class__
            name = f"{cl}_{ORDERS[cl]}"
            self._objects[name] = o
            ORDERS[cl] += 1

        for name, o in kwobjs.items():  # type: object
            self._objects[name] = o
        
        # bind methods
        # Assume all objects has same methods
        all_method = dir(o)
        self._recursion_level -= 1
        if self._recursion_level >= 0:
            for m in all_method:
                if m.startswith("_"):
                    continue

                _type = type(getattr(o, m))
                if _type in [types.MethodType]:
                    logging.debug(f"Binding {m} type {_type}.")

                    def wrapper(*args, **kwargs):
                        return partial(self._method_all, name_method=m)

                    setattr(self, m, wrapper())

                else:  # objects or fields
                    # TODO: stack overflow for plain fields
                    print(f"Binding {m} with type {_type}.")
                    subs = [getattr(o, m) for n, o in self._objects.items()]
                    sub = Comp(*subs, recursion_level=0)
                    setattr(self, m, sub)

    @property
    def objects(self):
        return self._objects
    
    def _method_all(self, *args, name_method, **kwargs):
        results = {}
        logging.debug(f">>> {name_method = }")
        for name, o in self._objects.items():
            _callable = getattr(o, name_method)
            results[name] = _callable(*args, **kwargs)
        
        return results


if __name__ == '__main__':

    import pandas as pd 
    a = pd.Series([1,2,3])
    b = pd.Series([1,2,3])
    c = Comp(a, b)
    c.shift(1)
    c.sum()
    # we cannot do this yet...
    # c.mean() + c.std()
    # c.plot()