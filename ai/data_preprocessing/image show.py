import cv2
import numpy as np
import os
import json
from PIL import Image, ImageDraw



def draw_yolo_bbox(image_path, annotation_path):
    # Open the image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Read annotation file and draw bounding boxes
    with open(annotation_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            class_id, x, y, w, h = map(float, line.strip().split())

            # Convert YOLO coordinates to pixel values
            image_width, image_height = image.size
            bbox_x = int(x * image_width)
            bbox_y = int(y * image_height)
            bbox_width = int(w * image_width)
            bbox_height = int(h * image_height)

            # Calculate bounding box coordinates
            x_center = bbox_x
            y_center = bbox_y
            x_min = x_center - bbox_width/2
            x_max = x_center + bbox_width/2
            y_min = y_center - bbox_height/2
            y_max = y_center + bbox_height/2

            print(x_center, y_center, bbox_width, bbox_height)
            print('image width, height:', image_width, image_height)



            # Draw the bounding box
            draw.rectangle([x_min, y_min, x_max, y_max], outline='red', width=3)

    return image


def get_image_paths(folder_path, extensions=[".tiff"]):
    image_paths = []
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            if any(filename.lower().endswith(ext) for ext in extensions):
                image_paths.append(os.path.join(dirpath, filename))
    return image_paths


image_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/철근노출/700x700_image"
real_image_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/철근노출/[원천]콘크리트_철근노출_원천_08"
annotation_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/철근노출/700x700_label"
real_annotation_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/철근노출/[라벨]콘크리트_철근노출_라벨링_01"

# 이미지 폴더의 모든 파일 목록 가져오기
image_files = os.listdir(image_folder)
real_image_files = os.listdir(real_image_folder)

image_path = []
yolo_annotation_path = []
real_annotation_path = []
real_image_path = []

for image_file in image_files:
    image_name = os.path.splitext(image_file)[0]  # 이미지 파일 이름 (확장자 제외)
    annotation_file = image_name + ".txt"  # 해당하는 어노테이션 파일 이름
    real_annotation_file = image_name + '.json'

    real_image_path.append(os.path.join(real_image_folder, image_file))
    image_path.append(os.path.join(image_folder, image_file))  # 이미지 파일 경로
    yolo_annotation_path.append(os.path.join(annotation_folder, annotation_file))  # 어노테이션 파일 경로
    real_annotation_path.append(os.path.join(real_annotation_folder, real_annotation_file))

    #print("이미지 경로:", image_path)
    #print("어노테이션 파일 경로:", yolo_annotation_path)



# Example usage
k=165
print(image_path[k])
print(yolo_annotation_path[k])
print(real_annotation_path[k])

output_image = draw_yolo_bbox(image_path[k], yolo_annotation_path[k])
output_image.show()  # Display the image with the drawn bounding boxes

real_output_image = draw_yolo_bbox(real_image_path[k], yolo_annotation_path[k])
real_output_image.show()  # Display the image with the drawn bounding boxes

with open(f'{real_annotation_path[k]}', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('real:',data)



file = open(yolo_annotation_path[k], "r")
content = file.read()
print('resize:',content)



1126.67, 6.67, 243.33, 413.33
1043.33, 423.33, 183.33, 403.33
986.67, 820, 160, 340
