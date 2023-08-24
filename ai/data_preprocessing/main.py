import xml.etree.ElementTree as ET
import json
import os



folder_path = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/박리/이미지가 존재하는 label"



##---------------------------JSON 따옴표 변환--------------------##

"""
def fix_json_quotes(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()

    # Replace single quotes with double quotes
    data = data.replace("'", '"')

    # Write back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(data)

folder_path = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/[라벨]콘크리트_철근노출_라벨링_01"

for dirpath, dirnames, filenames in os.walk(folder_path):
    for filename in filenames:
        if filename.endswith('.json'):  # Process only JSON files
            file_path = os.path.join(dirpath, filename)
            fix_json_quotes(file_path)



"""
##------------------------------------------------------------##


##----------------JSON 들여쓰기 삭제----------------------------##
"""
def fix_json_format(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove all newlines and whitespace
    content = content.replace('\n', '').replace('\r', '').replace('\t', '').replace(' ', '')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

folder_path = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/[라벨]콘크리트_철근노출_라벨링_01"

for dirpath, dirnames, filenames in os.walk(folder_path):
    for filename in filenames:
        if filename.endswith('.json'):  # Process only JSON files
            file_path = os.path.join(dirpath, filename)
            fix_json_format(file_path)
"""
##------------------------------------------------------------##


file_paths = []

class_mapping = {
    'Exposure': 0,
    'ConcreteCrack': 1,
    'Spalling': 2
}


for dirpath, dirnames, filenames in os.walk(folder_path):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        file_paths.append(file_path)

print(len(file_paths))

print(file_paths[0])

for i in range(0, len(file_paths)):
    with open(f'{file_paths[i]}', 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            #print('JSON Decode Error:', e)
            #print('File path:', file_paths[i])
            #print('File content:', f.read())
            #print('에러가 발생한 i:', i)
            continue  # Skip to the next file

    annotations = data['annotations']
    detail = data['images']
    num_object = len(annotations)
    object_info = []

    for j in range(0, num_object):
        annotation_info = annotations[j]

        label = annotation_info['attributes']['class']

        if label == 'Spalling':
            image_width = data['images'][0]['width']
            image_height = data['images'][0]['height']

            object_class = class_mapping[label]



            bbox_x = annotation_info['bbox'][0]
            bbox_y = annotation_info['bbox'][1]
            bbox_width = annotation_info['bbox'][2]
            bbox_height = annotation_info['bbox'][3]


            # 이 공식이 맞음!!!!!!!! 이걸로 해 제발제발
            # bbox[0]은 x_center가 아니고 x_min임!!!! -8/23 확인
            x_min = bbox_x
            x_max = x_min + bbox_width
            y_min = bbox_y
            y_max = y_min + bbox_height


            ## YOLO format : class_id center_x center_y width height

            yolo_x_center = round(((x_max+x_min)/2)/image_width,6)
            yolo_y_center = round(((y_max+y_min)/2)/image_height,6)
            yolo_width = round(bbox_width/image_width,6)
            yolo_height = round(bbox_height/image_height,6)

            result = []
            result.append(yolo_x_center)
            result.append(yolo_y_center)
            result.append(yolo_width)
            result.append(yolo_height)


            object_info.append(f'{object_class} {" ".join(map(lambda x: str(float(x)), result))}')

    image_info = '\n'.join(object_info)
    file_name = data['images'][0]['file_name']
    txt_file_name = os.path.splitext(file_name)[0] + ".txt"


    storage_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/박리/resized_label"
    final_path = os.path.join(storage_folder, txt_file_name)

    print(image_info)
    print("#----------------------#")

    #print(object_info)
    #print(i)
    with open(final_path, 'w') as f:
        f.write(image_info)
"""

with open(f'{file_paths[7]}', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(len(data['annotations']))
print(data['annotations'][7])
"""