
# 1) Tortilla (16) - cutting board (21)
# 2) Knife (20) - butter (17)
# 3) Tortilla (16) - Knife (20) - butter (17)
# 4) Knife (20) - Paper towel (23) - Paper sheet (26)
# 5) Knife (20) - Jam (18)
# 6) Tortilla (16) - Knife (20) - Jam (18)
# 7) Tortilla (16)
# 8) Tortilla (16) - Toothpick (19)
# 9) Tortilla (16) - Knife (20)
# 10) Tortilla (16)
# 11) Tortilla Pieces (25) - Dental floss (22)
# 12) Tortilla Pieces (25) - Plate (24)


# 1) measuring cup (2) - bottle (11)
# 2) electric kettle (1) - bottle (11)
# 3) filter cone dripper (5) - coffee mug (7)
# 4) paper basket filter (6) - half paper filter (14)
# 5) paper basket filter (6) - half paper filter (14) - quarter paper filter (15)
# 6) filter cone dripper (5) - paper basket filter (6)
# 7) spoon (9) - bowl (10) - coffee bean (?)
# 8) kitchen scale (3) - spoon (9) - bowl (10) - coffee bean (?)
# 9) coffee grinder (4) - spoon (9) - bowl (10) - coffee bean (?)
# 10) coffee grinder (4) - timer (?)
# 11) coffee grinder (4) - filter cone dripper (5) - paper basket filter (6) - spoon (9)
# 12) electric kettle (1) - thermometer (8)
# 13) electric kettle (1) - filter cone dripper (5) - paper basket filter (6)
# 14) electric kettle (1) - filter cone dripper (5) - paper basket filter (6)
# 15) filter cone dripper (5) - paper basket filter (6)
# 16) coffee mug (7)

# task = 'coffee'
task = 'pinwheel'

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

pinwheel_objects = [
    [16, 21],      # 1
    [20, 17],      # 2
    [16, 20, 17],  # 3
    [20, 23, 26],  # 4
    [20, 18],      # 5
    [16, 20, 18],  # 6
    [16],          # 7
    [16, 19],      # 8
    [16, 20],      # 9
    [16],          # 10
    [25, 22],      # 11
    [25, 24],      # 12
]

coffee_objects = [
    [2, 11],       # 1
    [1, 11],       # 2
    [5, 7],        # 3
    [6, 14],       # 4
    [6, 14, 15],   # 5
    [5, 6],        # 6
    [9, 10],       # 7
    [3, 9, 10],    # 8
    [4, 9, 10],    # 9
    [4],           # 10
    [4, 5, 6, 9],  # 11
    [1, 8],        # 12
    [1, 5, 6],     # 13 
    [1, 5, 6],     # 14
    [5, 6],        # 15
    [7],           # 16
]


step_object = [
    [16, 21],      # 1
    [20, 17],      # 2
    [16, 20, 17],  # 3
    [20, 23, 26],  # 4
    [20, 18],      # 5
    [16, 20, 18],  # 6
    [16],          # 7
    [16, 19],      # 8
    [16, 20],      # 9
    [16],          # 10
    [25, 22],      # 11
    [25, 24],      # 12
]


if (task == 'coffee'):
    step_object = coffee_objects
elif (task == 'pinwheel'):
    step_object = pinwheel_objects


task_related_aoi = []

import pandas as pd


df = pd.read_csv('fixation_result.csv')

for index, row in df.iterrows():
    step_related_objects = step_object[int(row['Step Number']) - 1]
    if row['category_id'] in step_related_objects:
        task_related_aoi.append('Yes')
    else:
        task_related_aoi.append('No')

df['step_related_AOI'] = task_related_aoi
if "Unnamed: 0" in df:
    df.pop("Unnamed: 0")

df = df.drop_duplicates()


df.to_csv('task_aoi.csv', index=False)
