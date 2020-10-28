import pandas as pd
df = pd.DataFrame(data.data, columns=data.feature_names) #u
sing houses data
df['target'] = data.target
df.head()
