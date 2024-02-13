import pandas as pd


df = pd.read_csv("subject5_pinwheel_task_aoi.csv")

df = df.drop_duplicates()

df.to_csv('final_no_duplicate_result.csv', index=False)
