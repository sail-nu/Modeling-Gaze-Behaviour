import pandas as pd

df = pd.read_csv('task_aoi.csv')


df = df.drop_duplicates()

number_of_frames = len(pd.unique(df['image_id']))

df = df.loc[df['fixated'] == True]

number_of_fixated_frames = len(pd.unique(df['image_id']))

first_cateogry_rows = df.loc[(df['colision'] == True) & (df['step_related_AOI'] == 'Yes')]
first_cateogry_frame_numbers = list(set(first_cateogry_rows['image_id'].values.tolist()))

second_condtion_rows = df.loc[(df['colision'] == True)]
# second_condition_frame_numbers = pd.unique(second_condtion_rows['image_id'])
second_condition_frame_numbers = list(set(second_condtion_rows['image_id'].values.tolist()))
second_category_frame_numbers = [x for x in second_condition_frame_numbers if x not in first_cateogry_frame_numbers]

print('Number of frames are = ', number_of_frames)
print('Number of fixated frames are = ', number_of_fixated_frames)
print('Number of (colision + AOI) true frames are = ', len(first_cateogry_frame_numbers))
print('Number of (colision) true frames are = ', len(second_category_frame_numbers))

print('Percentage of total fixated frames is = {} %'.format(number_of_fixated_frames / number_of_frames * 100))
print('Percentage of Non-Step-related fixated frames when gaze collide with object bounding box is = {} %'.format(len(second_category_frame_numbers) / number_of_frames * 100))
print('Percentage of Step-related fixated frames when gaze collide with object bounding box is = {} %'.format(len(first_cateogry_frame_numbers) / number_of_frames * 100))
