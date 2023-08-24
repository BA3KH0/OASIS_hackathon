import json
import os
import shutil

image_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/박리/resized_image"  # 이미지 파일들이 있는 폴더 경로
label_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/박리/resized_label"  # 레이블 파일들이 있는 폴더 경로

image_files = os.listdir(image_folder)  # 이미지 파일 목록 가져오기
label_files = os.listdir(label_folder)  # 레이블 파일 목록 가져오기



no_label = []
no_image = []

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



print(no_label)

# 레이블 파일이 없는 이미지 제거
folder_path = image_folder  # 파일들이 있는 폴더 경로

for file_name in no_label:
    file_path = os.path.join(folder_path, file_name)  # 파일 경로 생성
    print(file_path)
    if os.path.exists(file_path):  # 파일이 존재하는 경우에만 제거
        os.remove(file_path)  # 파일 제거
        print(f'{file_name} 파일을 제거했습니다.')
    else:
        print(f'{file_name} 파일이 존재하지 않습니다.')
    


"""
# 이미지 파일이 없는 레이블 제거
folder_path = label_folder  # 파일들이 있는 폴더 경로

for file_name in no_image:
    file_path = os.path.join(folder_path, file_name)  # 파일 경로 생성
    print(file_path)
    if os.path.exists(file_path):  # 파일이 존재하는 경우에만 제거
        os.remove(file_path)  # 파일 제거
        print(f'{file_name} 파일을 제거했습니다.')
    else:
        print(f'{file_name} 파일이 존재하지 않습니다.')
        
"""