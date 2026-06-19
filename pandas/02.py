import pandas as pd

df = pd.read_csv('workoutdata.csv')

new_df = df.dropna()

print(new_df.to_string())

print(df.duplicated())
