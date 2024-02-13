from cmath import nan
from operator import le
import pandas as pd
import math

df = pd.read_csv('subject16_pinwheel_task_aoi.csv', index_col=None)
df = df.drop_duplicates(keep='first')

df = df[(df['step_related_AOI'] == 'Yes') & (df['fixated'] == True)]

df['timestamp_diff'] = df['gaze_timestamp_unix'].diff()

df = df[['image_id', 'category', 'category_id', 'gaze_timestamp_unix', 'timestamp_diff', 'Step Number']]
df = df.loc[df['timestamp_diff'] > 0]

step_asd_list = []
for i in range(1, 17):
    df_particular_step = df.loc[df['Step Number'] == int(i)]
    if (int(i) != 1):
        df_particular_step = df_particular_step.tail(-1)
    step_asd = df_particular_step['timestamp_diff'].mean()
    if (math.isnan(step_asd) == False):
        step_asd_list.append(step_asd)

final_asd = (sum(step_asd_list) / len(step_asd_list))
print('final_asd = ', final_asd)

df.to_csv("asd_result.csv", index=False)
