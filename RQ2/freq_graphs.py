import pandas as pd

df = pd.read_csv('merged_files.csv')

df = df[df['colision'] == True]
df = df.filter(items=['category', 'category_id'])

objects = [
    "electric kettle", 
    "liquid measuring cup",
    "kitchen scale",
    "coffee grinder",
    "filter cone dripper",
    "paper basket filter",
    "coffee mug",
    "thermometer",
    "spoon",
    "bowl",
    "bottle",
    "hand",
    "left",
    "half paper filter",
    "quarter paper filter",
    "tortilla",
    "peanut butter",
    "fruit jam",
    "toothpick",
    "butter knife",
    "chopping board",
    "dental floss",      
    "paper towel",
    "plate",
    "tortilla pieces",
    "paper sheet",
    "",
    "stop sign",
    "parking meter",
    "bench",
]

        
category_id_list = df['category_id'].tolist()
highest_category_number = max(category_id_list)
category_id_list = [x - 1 for x in category_id_list]

result_list = [ [0] * 104 for i in range(104)]

df_result = pd.DataFrame()


for i in range(0, len(category_id_list) - 1):
    result_list[category_id_list[i]][category_id_list[i+1]] += 1

for i in range(0, highest_category_number):
    for j in range(0, highest_category_number):
        if (i != j):
            new_row = {
                'From_AOI_Category_Id':  i + 1, 
                'From_AOI_Category': objects[i],
                'To_AOI_Category_Id': j + 1,
                'To_AOI_Category': objects[j], 
                'Frequency': result_list[i][j]}
            df_result = df_result.append(new_row, ignore_index = True)

df_result.to_csv('frequency_result.csv', index=False)


# Graph Visualization

df_result_filtered = df_result[df_result['Frequency'] > 0]
df_result_filtered['Frequency'] = df_result_filtered['Frequency'].div(15)

import networkx as nx
import matplotlib.pyplot as plt


G = nx.from_pandas_edgelist(
    df_result_filtered,
    source='From_AOI_Category',
    target='To_AOI_Category',      
    edge_attr=["Frequency"],
)

scaled_degree = [d[1] * 0.05 for d in nx.degree(G)]
nx.draw(G,
        width=list(nx.get_edge_attributes(G, 'Frequency').values()),
        # node_size=scaled_degree,
        node_color=scaled_degree,
        edge_color='red',
        cmap='terrain',
        with_labels=True,
        )

plt.show()



