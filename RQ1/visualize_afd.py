from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('fixation_result.csv', index_col=None)

# mean_duration = df.groupby(['step_number', 'step_related_AOI'])['fixation_duration'].mean()

# mean_duration.to_csv('result_file.csv')

# df_pivot = pd.pivot_table(
#     df, 
#     values="fixation_duration",
#     index="step_number",
#     columns="step_related_AOI", 
#     aggfunc=np.mean
# )

# plt.rcParams['xtick.major.pad']='8'

df_step_one = df.loc[df['step_number'] == 1]

# df_step_related_yes = df.loc[df['step_related_AOI'] == True]
# df_step_related_no = df.loc[df['step_related_AOI'] == False]

df_temp = df_step_one.groupby(['category'])['fixation_duration'].mean()

print(df_temp)

# color_list = ["r", "g"]

# ax = df_temp.plot.bar(x='category', y='fixation_duration', color=color_list, rot=0)
# fig = ax.get_figure()
# fig.set_size_inches(50, 40)
# fig.savefig("savefig2.png")


# mean_duration2 = df_step_one.groupby(['category'])['fixation_duration'].mean()

# highlight_color = np.where(df["step_related_AOI"], "red", "blue")

# df_pivot = pd.pivot_table(
#     df, 
#     values="fixation_duration",
#     index="category",
#     # columns="step_related_AOI", 
#     aggfunc=np.mean,
#     color='red'
# )



# ax = df_pivot.plot(kind="bar")

# fig = ax.get_figure()

# fig.set_size_inches(10, 9)

# ax.set_xlabel("category")
# ax.set_ylabel("Average Fixxation Duration")
# fig.savefig("savefig.png")


df_pivot = df_step_one.groupby("category").apply(lambda x: pd.Series({
    "mean_duration": x["fixation_duration"].mean(),
    "color": "red" if any(x["step_related_AOI"] == 'No') else "blue"
}))


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True


fig = plt.figure()
# ax.set_xlabel('x-axis', fontsize = 12)
# ax.set_ylabel('y-axis', fontsize = 10)

# spacing = 0.100
# fig.subplots_adjust(bottom=spacing)

plt.bar(df_pivot.index, df_pivot["mean_duration"], color=df_pivot["color"])

# df_step_one = df_step_one.groupby(['category'])['fixation_duration'].mean()
# df_step_one['fixation_duration'].reset_index().plot(kind="bar", color=['black', 'red', 'black', 'red', 'black'])


plt.show()