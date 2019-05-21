import pandas as pd
import numpy as np
a = np.arange(9).reshape(3,3)
df = pd.DataFrame(a,columns=["A","B","C"])
print(df)
dfRatings