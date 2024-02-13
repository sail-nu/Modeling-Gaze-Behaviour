import pandas as pd
df1 = pd.read_csv('bbox-sheet.csv')
df2 = pd.read_csv('gaze_result.csv')
df3 = pd.read_csv('pupil_result.csv')
merged_df1 = pd.merge(df1, df2, left_on='image_id', right_on='world_index', how='inner')
merged_df2 = pd.merge(merged_df1, df3, left_on='image_id', right_on='pupil_index', how='inner')
merged_df2.to_csv('merged_files.csv', index=False)