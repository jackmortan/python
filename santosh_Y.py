import pandas as pd, csv

df = pd.read_excel('/Users/shahajisargar/code/Receipt Monthly Report.xlsx')
values_to_delete = ['Actual', '365 Accuracy(%)', '275 Accuracy(%)','90 Accuracy(%)','30 Accuracy(%)']
mask = df['Measure Names'].isin(values_to_delete) 
df.drop(df[mask].index, inplace=True)
df.to_excel('/Users/shahajisargar/code/new_data1.xlsx', index=False)


