from cmath import nan
from operator import le
import pandas as pd
import math

df = pd.read_csv('subject5_coffee_fixations.csv', index_col=None)
df = df.drop_duplicates(keep='first')

df['timestamp_diff'] = df['start_timestamp'].diff()

df = df[['id', 'start_frame_index', 'end_frame_index', 'start_timestamp', 'timestamp_diff', 'duration']]

final_asd = df['timestamp_diff'].mean()
print('final_asd = ', final_asd * 1000)

df.to_csv("pupil_asd.csv", index=False)
