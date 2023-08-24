import os

image_dir = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/최종/train_image"  # 이미지 파일들이 있는 폴더 경로
label_dir = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/최종/train_label"  # 레이블 파일들이 있는 폴더 경로

image_files = os.listdir(image_dir)
label_files = os.listdir(label_dir)

image_names = [os.path.splitext(f)[0] for f in image_files if f.endswith(".tiff")]
label_names = [os.path.splitext(f)[0] for f in label_files if f.endswith(".txt")]

if set(image_names) == set(label_names):
    print("모든 이미지 파일과 라벨 파일이 서로 완벽하게 일치합니다.")
else:
    print("이미지 파일과 라벨 파일이 서로 일치하지 않습니다.")
