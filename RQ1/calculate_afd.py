from cmath import nan
import pandas as pd
from statistics import mean
import math 

df = pd.read_csv('subject16_pinwheel_task_aoi.csv', index_col=None)


df = df.drop_duplicates(keep='first')

# mean_duration = df.groupby(['step_number', 'step_related_AOI'])['fixation_duration'].mean()

def Average(lst):
    return sum(lst) / len(lst)


df.groupby("image_id")['fixation_duration'].mean() 

step_mean_fixation = []
non_step_mean_fixation = []
for i in range(1, 17):
    # df_particular_step = df.loc[df['Step Number'] == int(i)]

    # df_related_step = df_particular_step[(df_particular_step['step_related_AOI'] == 'Yes') & (df_particular_step['fixated'] == True)]
    # related_step_fix_mean = df_related_step['fixation_duration'].mean()
    # print(related_step_fix_mean)
    # if (math.isnan(related_step_fix_mean) == False):
    #     step_mean_fixation.append(related_step_fix_mean)

    # df_non_related_step = df_particular_step[(df_particular_step['step_related_AOI'] == 'No') & (df_particular_step['fixated'] == True)]
    # non_related_step_fix_mean = df_non_related_step['fixation_duration'].mean()
    # if (math.isnan(non_related_step_fix_mean) == False):
    #     non_step_mean_fixation.append(non_related_step_fix_mean)

    df_related_step = df_particular_step[(df_particular_step['fixated'] == True)]
    related_step_fix_mean = df_related_step['fixation_duration'].mean()
    sss.spends
    print(related_step_fix_mean)
    if (math.isnan(related_step_fix_mean) == False):
        step_mean_fixation.append(related_step_fix_mean)

    # df_temp = df_particular_step.groupby(['step_related_AOI'])['fixation_duration'].mean()

step_average = Average(step_mean_fixation)
# non_step_average = Average(non_step_mean_fixation)


