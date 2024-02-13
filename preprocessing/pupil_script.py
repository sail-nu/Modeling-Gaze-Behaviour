import pandas as pd
import csv
 
df = pd.read_csv("pupil_positions.csv")

df = df.loc[df['confidence'] > 0.6]
df_index = df.groupby(['world_index']) 
df_mean = df.groupby(['world_index'])['diameter'].mean()
df_std = df.groupby(['world_index'])['diameter'].std()

df_result = pd.DataFrame()
df_result['pupil_index'] = df['world_index'].unique()
df_result['pupil_diameter_mean'] = df_mean
df_result['pupil_diameter_std'] = df_std

df_result.to_csv('pupil_result.csv', index=False)
