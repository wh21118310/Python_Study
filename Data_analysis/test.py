import pandas as pd
import numpy as np
df = pd.DataFrame({'key':['one', 'three', 'two', 'two', 'one','three','three','two','one','one'],
'data1':np.random.randint(25,75,size=10),'data2':np.random.randint(1,50,size=10),'data3':np.random.randint(50,100,size=10),'data4':np.random.randint(100,150,size=10)})
def get_data1_group(data):
	if data <60:
		data_group = 'bad'
	else:
		data_group = 'good'
	return data_group
data1 = df.set_index('data1')
print(data1.groupby(get_data1_group).size())
