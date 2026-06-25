import pandas as pd
import glob as glob

files = glob.glob('data/*.csv')
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

df = df[df['product'] == 'pink morsel']
df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)
df['sales'] = df['price'] * df['quantity']

result = df[['sales', 'date', 'region']]

result.to_csv('./output/task2.csv', index=False)