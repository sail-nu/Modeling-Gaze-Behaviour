import pandas as pd
import numpy as np
import csv
 

df_fixation = pd.read_csv("subject3_pinwheel_fixations.csv")
df_task_aoi = pd.read_csv("task_aoi.csv")
df_task_aoi = df_task_aoi.drop_duplicates(keep='last')


fixation_frames = []
fixation_duration = {}


for index, row in df_fixation.iterrows():
    start_frame_index = row['start_frame_index']
    end_frame_index = row['end_frame_index']
    for i in range(int(start_frame_index), int(end_frame_index) + 1):
        fixation_frames.append(i)
        fixation_duration.update({i: row['duration']})

merged_fixated_list = []

fixation_duration_result = []

for index, row in df_task_aoi.iterrows():
    if row['image_id'] in fixation_duration:
        fixation_duration_result.append(fixation_duration.get(row['image_id']))
    else:
        fixation_duration_result.append(0)

    if (int(row['image_id']) not in fixation_frames):
        merged_fixated_list.append(False)
    else:
        merged_fixated_list.append(True)

df_task_aoi['fixated'] = merged_fixated_list
df_task_aoi['fixation_duration'] = fixation_duration_result


df_task_aoi.to_csv("fixation_result.csv", index=False)

