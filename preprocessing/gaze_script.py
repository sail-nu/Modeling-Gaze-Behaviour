import pandas as pd
import csv
 
# creating a data frame
df = pd.read_csv("gaze_positions.csv")

# df = df.loc[df['confidence'] > 0.6]
df = df.loc[df.groupby(['world_index'])['confidence'].idxmax()]
df['gaze_pos_x'] = df['norm_pos_x'] * 1280
df['gaze_pos_y'] = df['norm_pos_y'] * 720
df = df.filter(items=['world_index', 'gaze_pos_x', 'gaze_pos_y'])


t = open('gaze_result.csv', 'w')

# csv_writer = csv.writer(t)
# csv_header = ['gaze_pos_x', 'gaze_pos_y', 'world_index']
# csv_writer.writerow(csv_header)

df.to_csv('gaze_result.csv', index=False)


