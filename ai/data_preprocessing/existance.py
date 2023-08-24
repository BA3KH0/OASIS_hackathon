import json
import os
import shutil

image_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/콘크리트/[원천]콘크리트_콘크리트균열_원천_34"  # 이미지 파일들이 있는 폴더 경로
label_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/콘크리트/YOLO label folder"  # 레이블 파일들이 있는 폴더 경로

image_files = os.listdir(image_folder)  # 이미지 파일 목록 가져오기
label_files = os.listdir(label_folder)  # 레이블 파일 목록 가져오기

no_label = []
no_image = []

print('-------------------------------------')

for image_file in image_files:
    image_name = os.path.splitext(image_file)[0]  # 이미지 파일 이름 가져오기
    label_file = image_name + ".txt"  # 해당 이미지와 일치하는 레이블 파일 이름 생성

    if label_file not in label_files:
        no_label.append(f'{image_file}')
        print(f"레이블 파일이 없는 이미지: {image_file}")

for label_file in label_files:
    label_name = os.path.splitext(label_file)[0]  # 레이블 파일 이름 가져오기
    image_file = label_name + ".tiff"  # 해당 레이블과 일치하는 이미지 파일 이름 생성

    if image_file not in image_files:
        no_image.append(f'{label_file}')
        print(f"이미지 파일이 없는 레이블: {label_file}")


print('레이블 파일이 없는 이미지 총 개수: ', len(no_label))
print('이미지 파일이 없는 레이블 총 개수: ', len(no_image))
