import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Sample DataFrame
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

G = nx.Graph()

# Adding nodes
for index, row in df.iterrows():
    G.add_node(row['Node'], value=row['Value'])

# Adding edges based on distance
for i in range(len(df)):
    for j in range(i + 1, len(df)):
        node1 = df.iloc[i]['Node']
        node2 = df.iloc[j]['Node']
        distance = abs(df.iloc[i]['Value'] - df.iloc[j]['Value'])
        G.add_edge(node1, node2, weight=distance)

# Plotting the scan path graph
pos = nx.spring_layout(G)  # Positioning nodes
labels = nx.get_node_attributes(G, 'value')
weights = nx.get_edge_attributes(G, 'weight')

nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12)
nx.draw_networkx_labels(G, pos, labels=labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

plt.title('Scan Path Graph')
plt.axis('off')
plt.show()
