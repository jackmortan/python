import pandas as pd

df = pd.read_excel('/Users/shahajisargar/Downloads/Query_202331_162514_Details_export_1677668132986.xlsx')
range_data = df.iloc[:, [1]]
data = pd.DataFrame(range_data)
# Convert the date string to a datetime object
df['Date'] = pd.to_datetime(data['Date'])
# Convert the datetime object to a string in the desired format
df['Date'] = df['Date'].dt.strftime('%B %Y')
print(df)
