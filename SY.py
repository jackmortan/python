import pandas as pd 

data = (r'/Users/shahajisargar/Downloads/Query_202331_162514_Details_export_1677668132986.xlsx')
df1 = pd.read_excel(data)
range_data = df1.iloc[:, [1]]
data = pd.DataFrame(range_data)
df1['Date'] = pd.to_datetime(data['Date'])
df1['Date'] = df1['Date'].dt.strftime('%B %Y')
df1.drop(['Forecast_ID','30_Accuracy(%)','90_Accuracy(%)','365_Accuracy(%)','Insertdatetime','275_Accuracy'], axis=1,inplace=True)
df1.rename(columns={'Date':'MONTH(Date)'}, inplace = True)
a1=df1[df1['Type']=='Other']
a1=a1[a1['Model']=='5268AC']
# print(a1)

df2 = pd.read_excel(r'/Users/shahajisargar/Downloads/Receipt Monthly Report.xlsx')
values_to_delete = ['Actual', '365 Accuracy(%)', '275 Accuracy(%)','90 Accuracy(%)','30 Accuracy(%)']
mask = df2['Measure Names'].isin(values_to_delete)
df2.drop(df2[mask].index, inplace=True)
df2['Measure Values'] =df2['Measure Values'].astype('int64')
a=df2[df2['Measure Names']=='30 Days']
a.rename(columns={'Measure Values':'30 Days'}, inplace = True)
a.drop('Measure Names',axis=1,inplace=True)
# days_30 = a['30 Days']
b=df2[df2['Measure Names']=='90 Days']
b.rename(columns={'Measure Values':'90 Days'}, inplace = True)
b.drop('Measure Names',axis=1,inplace=True)
# days_90 = b['90 Days']
c=df2[df2['Measure Names']=='275 Days']
c.rename(columns={'Measure Values':'275 Days'}, inplace = True)
c.drop('Measure Names',axis=1,inplace=True)
# days_275 = c['275 Days']
d=df2[df2['Measure Names']=='365 Days']
d.rename(columns={'Measure Values':'365 Days'}, inplace = True)
d.drop('Measure Names',axis=1,inplace=True)
# days_365 = d['365 Days']
col1 = pd.concat([a['30 Days'], b['90 Days'], c['275 Days'], d['365 Days']], axis=1)
# print(col1)
newdf1 = a.merge(b, how='right')
newdf2 = b.merge(a,how='left')
newdf3 = c.merge(d, how='right')
newdf4 = d.merge(c,how='left')
x = pd.DataFrame(newdf1,newdf2)
y = pd.DataFrame(newdf3,newdf4)
result_df = pd.concat([x, y], axis=0)

print(result_df)

# print(days_30,days_90,days_275,days_365)
# c=df2[df2['Measure Names']=='275 Days']
# df2['275 Days'] = c
# d=df2[df2['Measure Names']=='365 Days']
# df2['365 Days'] = d


# print(a)
# print(b)
# df = pd.concat([df2, new_cols], axis=1)



# print(df)


