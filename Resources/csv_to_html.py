import pandas as pd
# read csv file
df = pd.read_csv('../cities.csv')
# dave the df to a file
df.to_html('cities.html',index=False)
# assign to string
cities = df.to_html()
print(cities)