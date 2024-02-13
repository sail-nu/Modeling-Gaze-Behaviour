
import pandas as pd

df = pd.read_csv('merged_files.csv')

colision_list = []

for index, row in df.iterrows():
    if ((row['gaze_pos_x'] >= row['top_left_x']) and (row['gaze_pos_x'] <= (row['top_left_x'] + row['width'])) and 
        (row['gaze_pos_y'] >= row['top_left_y']) and (row['gaze_pos_y'] <= (row['top_left_y'] + row['height']))):
        colision_list.append('True')
    else:
        colision_list.append('False')

df['colision'] = colision_list
df.to_csv('merged_files.csv', index=False)

