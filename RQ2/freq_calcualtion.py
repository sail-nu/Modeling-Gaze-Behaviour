import pandas as pd
df = pd.read_csv('merged_files.csv')
df = df[df['colision'] == True]
df = df.filter(items=['category', 'category_id'])
objects = [
    "Electric Kettle", 
    "Measuring Cup",
    "Kitchen Scale",
    "Grinder",
    "Filter Dripper",
    "Paper Filter",
    "Coffee Mug",
    "Thermometer",
    "Spoon",
    "Bowl",
    "Bottle",
    "Left Hand",
    "Right Hand",
    "Half Paper Filter",
    "quarter paper filter",
    "tortilla",
    "peanut butter",
    "fruit jam",
    "toothpick",
    "butter knife",
    "chopping board",
    "dental floss",      
    "Paper Towel",
    "Plate",
    "tortilla pieces",
    "paper sheet",
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

print(df_result['Frequency'].sum())



# Graph Visualization
    # df_result_filtered = df_result[df_result['Frequency'] > 0]
    # df_result_filtered['Frequency'] = df_result_filtered['Frequency'].div(15)
    # import networkx as nx
    # import matplotlib.pyplot as plt
    # G = nx.from_pandas_edgelist(
    #     df_result_filtered,
    #     source='From_AOI_Category',
    #     target='To_AOI_Category',      
    #     edge_attr=["Frequency"],
    # )
    # d = dict(G.degree)
    # scaled_degree = [d[1] * 0.1 for d in nx.degree(G)]
    # nx.draw(G,pos=nx.shell_layout(G),
    #         width=list(nx.get_edge_attributes(G, 'Frequency').values()),
    #         # node_size=scaled_degree,
    #         node_size=[v * 100 for v in d.values()],
    #         node_color='yellow',
    #         edge_color='cornflowerblue',
    #         cmap='terrain',
    #         with_labels=True,
    #         )

    # plt.show()
    # plt.savefig('new_plot.png')