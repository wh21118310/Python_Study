#coding:utf-8
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(0,150,size=(4,4)),index = ['第一季度','第二季度','第三季度','第四季度'],columns=[['python','python','机器学习','机器学习'],['初级','高阶','初级','高阶']])
print(df)
print(df.stack())



