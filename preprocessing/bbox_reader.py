import json
import csv
  
f = open('subject13-pinwheel-pred-active.json')
t = open('bbox-sheet.csv', 'w')

data = json.load(f)

csv_writer = csv.writer(t)

csv_header = ['image_id', 'top_left_x', 'top_left_y', 'width', 'height', 'category_id', 'category']
csv_writer.writerow(csv_header)


for i in data['annotations']:
    top_left_x = i['bbox'][0]
    top_left_y = i['bbox'][1]
    width = i['bbox'][2]
    height = i['bbox'][3]
    image_id = i['image_id']
    category_id = i['category_id']
    category = i['category']
    row_result = [image_id, top_left_x, top_left_y, width, height, category_id, category] 
    csv_writer.writerow(row_result)
  
f.close()
t.close()
