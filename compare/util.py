from typing import List, Union
from itertools import combinations
import pandas as pd


def pair(dfs: List[Union[pd.DataFrame, pd.Series]]):
    return list(combinations(dfs, 2))


def pairwise_op(df_pair, func: str, *args, **kwargs):
    res = []
    for df1, df2 in df_pair:
        _func = df1.__getattribute__(func)
        res.append(_func(df2, *args, **kwargs))
    return res


class Result:
    
    def __init__(self) -> None:
        pass


class DiffSeries:
    def __init__(self, *ss: List[pd.Series], **kss) -> None:
        self._ss = ss

    def abs(self):
        return DiffSeries([s.abs() for s in self._ss])


class DiffDataFrame:
    
    def __init__(self, *dfs: List[Union[pd.DataFrame]], **kdfs) -> None:
        self._dfs = dfs

    def corrwith(self):
        pass
