from PIL import Image
import os
import json
from pathlib import Path


image_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/콘크리트/[원천]콘크리트_콘크리트균열_원천_34"
image_resize_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/콘크리트/resized_image"
label_resize_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/콘크리트/700x700_label"
label_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/철근노출/이미지 존재하는 label만 추림"


# 이미지 폴더와 레이블 폴더의 파일 목록 가져오기
image_files = os.listdir(image_folder)
print(image_files[3390:3396])
print(image_files.index('101_ee946363-31d0-45c5-9132-3ef2964d72b3.tiff'))



# TIFF 이미지 불러오기
for i in range(3397, len(image_files)):
    image = Image.open(image_folder + '/' + image_files[i])

    new_width = 600
    new_height = int(image.height * (new_width / image.width))

    # 이미지 크기 조정
    resized_image = image.resize((new_width, new_height), Image.BICUBIC)  # 다른 보간 방법 시도 가능

    # 크기 조정된 이미지 저장
    output_path = os.path.join(image_resize_folder, image_files[i])
    resized_image.save(output_path)
    print('현재까지 완료 ', i)



file_paths = []

class_mapping = {
    'Exposure': 0,
    'ConcreteCrack': 1,
    'Spalling': 2
}




for dirpath, dirnames, filenames in os.walk(label_folder):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        file_paths.append(file_path)


"""
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

        if label == 'Exposure':
            image_width = data['images'][0]['width']
            image_height = data['images'][0]['height']

            object_class = class_mapping[label]



            x_center = annotation_info['bbox'][0]
            y_center = annotation_info['bbox'][1]
            bbox_width = annotation_info['bbox'][2]
            bbox_height = annotation_info['bbox'][3]



            ## YOLO format : class_id center_x center_y width height

            yolo_x_center = round((x_center)/image_width,6)
            yolo_y_center = round((y_center)/image_height,6)
            yolo_width = round((bbox_width)/image_width,6)
            yolo_height = round((bbox_height)/image_height,6)




            result = []
            result.append(yolo_x_center)
            result.append(yolo_y_center)
            result.append(yolo_width)
            result.append(yolo_height)


            object_info.append(f'{object_class} {" ".join(map(lambda x: str(float(x)), result))}')

    image_info = '\n'.join(object_info)
    file_name = data['images'][0]['file_name']
    txt_file_name = os.path.splitext(file_name)[0] + ".txt"


    storage_folder = label_resize_folder
    final_path = os.path.join(storage_folder, txt_file_name)

    print(image_info)
    print("#----------------------#")
    print('---------------------------------')
    print('---------------------------------')
    print('---------------------------------')

    #print(object_info)
    #print(i)
    with open(final_path, 'w') as f:
        f.write(image_info)
"""