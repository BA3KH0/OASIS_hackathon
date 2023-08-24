import xml.etree.ElementTree as ET
import json
import os
import shutil


# main.py에서 저장한 label.txt 파일들 중, image file이 존재하는 것만 따로 다른 폴더로 옮기기

image_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/박리/[원천]콘크리트_박리_원천_16"
label_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/박리/[라벨]콘크리트_박리_라벨링_01"
output_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/박리/이미지가 존재하는 label"

# 이미지 폴더와 레이블 폴더의 파일 목록 가져오기
image_files = os.listdir(image_folder)
label_files = os.listdir(label_folder)

# 이미지 폴더와 레이블 폴더의 파일 이름 비교하여 일치하는 파일 추출 및 복사
for label_file in label_files:
    file_name = os.path.splitext(label_file)[0]  # 파일 이름에서 확장자 제거
    if file_name + '.tiff' in image_files:  # 이미지 폴더에 일치하는 파일이 있는지 확인
        # 일치하는 파일을 출력 폴더로 복사
        shutil.copy2(os.path.join(label_folder, label_file), os.path.join(output_folder, label_file))
