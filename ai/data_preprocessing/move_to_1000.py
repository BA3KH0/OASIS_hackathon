import os
import random
import shutil

image_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/박리/resized_image"
label_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/박리/resized_label"

image_total = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/최종/전체_image"
label_total = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/최종/전체_label"

image_train = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/최종/train_image"
label_train = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/최종/train_label"

image_valid = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/최종/valid_image"
label_valid = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/최종/valid_label"



# 이미지 파일 목록 가져오기
image_files = os.listdir(image_folder)

# 랜덤하게 이미지 파일 선택
train_index = image_files[:-200]
valid_index = image_files[-200:]




## total
# 선택된 이미지 파일을 출력 폴더로 복사

for image_file in image_files:
    shutil.copy2(os.path.join(image_folder, image_file), os.path.join(image_total, image_file))

# 선택된 이미지 파일과 동일한 이름의 레이블 파일 추출하여 출력 폴더로 복사
for image_file in image_files:
    label_file = image_file.split('.')[0] + '.txt'  # 이미지 파일과 동일한 이름의 레이블 파일 생성
    shutil.copy2(os.path.join(label_folder, label_file), os.path.join(label_total, label_file))




## train
# 선택된 이미지 파일을 출력 폴더로 복사

for image_file in train_index:
    shutil.copy2(os.path.join(image_folder, image_file), os.path.join(image_train, image_file))

# 선택된 이미지 파일과 동일한 이름의 레이블 파일 추출하여 출력 폴더로 복사
for image_file in train_index:
    label_file = image_file.split('.')[0] + '.txt'  # 이미지 파일과 동일한 이름의 레이블 파일 생성
    shutil.copy2(os.path.join(label_folder, label_file), os.path.join(label_train, label_file))



## valid
# 선택된 이미지 파일을 출력 폴더로 복사
for image_file in valid_index:
    shutil.copy2(os.path.join(image_folder, image_file), os.path.join(image_valid, image_file))

# 선택된 이미지 파일과 동일한 이름의 레이블 파일 추출하여 출력 폴더로 복사
for image_file in valid_index:
    label_file = image_file.split('.')[0] + '.txt'  # 이미지 파일과 동일한 이름의 레이블 파일 생성
    shutil.copy2(os.path.join(label_folder, label_file), os.path.join(label_valid, label_file))

