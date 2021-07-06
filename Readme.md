# Compare

Originally, this tool is created to compare few pandas dataframes easily. Just think about how many times you do this:

```python
df1.sum().plot()
df2.sum().plot()
df3.sum().plot()
```

Would it be better to just do:

```python
dfs.sum().plot()
```

The question is HOW?

Currently we have this, but it is not good enough, as for pandas, it can chain operation yet...

```python
import pandas as pd 

from compare.core import Comp

a = pd.Series([1,2,3])
b = pd.Series([1,2,3])
c = Comp(a, b)
c.shift(1)
c.sum()
# we cannot do this yet...
# c.mean() + c.std()
# c.plot()
```

Requirements:

- Python version: 3.9
