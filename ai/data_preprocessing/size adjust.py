from PIL import Image, ImageDraw
import os



image_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/철근노출/철근노출_1000장_image"
annotation_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/철근노출/철근노출_1000장_label"
real_annotation_folder = "C:/Users/user/Desktop/건물 균열 탐지 이미지/Training/콘크리트/철근노출/[라벨]콘크리트_철근노출_라벨링_01"

# 이미지 폴더의 모든 파일 목록 가져오기
image_files = os.listdir(image_folder)


image_path = []
yolo_annotation_path = []
real_annotation_path = []



for image_file in image_files:
    image_name = os.path.splitext(image_file)[0]  # 이미지 파일 이름 (확장자 제외)
    annotation_file = image_name + ".txt"  # 해당하는 어노테이션 파일 이름
    real_annotation_file = image_name + '.json'

    image_path.append(os.path.join(image_folder, image_file))  # 이미지 파일 경로
    yolo_annotation_path.append(os.path.join(annotation_folder, annotation_file))  # 어노테이션 파일 경로
    real_annotation_path.append(os.path.join(real_annotation_folder, real_annotation_file))






def resize_image_and_bbox(image, bbox, target_size):
    # Resize the image
    resized_image = image.resize(target_size, Image.ANTIALIAS)

    # Update the bounding box coordinates
    image_width, image_height = image.size
    target_width, target_height = target_size
    x_scale = target_width / image_width
    y_scale = target_height / image_height

    bbox_x, bbox_y, bbox_width, bbox_height = bbox
    new_bbox_x = bbox_x * x_scale
    new_bbox_y = bbox_y * y_scale
    new_bbox_width = bbox_width * x_scale
    new_bbox_height = bbox_height * y_scale

    return resized_image, (new_bbox_x, new_bbox_y, new_bbox_width, new_bbox_height)


# Example usage
image_path = image_path[0]
annotation_path = yolo_annotation_path[0]

target_size = (512, 512)  # Set your target size here

# Load image and bounding box information
image = Image.open(image_path)
with open(annotation_path, 'r') as f:
    annotation_data = f.readline().strip().split()
    bbox = list(map(float, annotation_data[1:]))  # assuming format is class x y w h

# Resize image and adjust bounding box
resized_image, resized_bbox = resize_image_and_bbox(image, bbox, target_size)

# Draw bounding box on the resized image
draw = ImageDraw.Draw(resized_image)
x, y, width, height = resized_bbox
x_min = int(x - width / 2)
y_min = int(y - height / 2)
x_max = int(x_min + width)
y_max = int(y_min + height)
draw.rectangle([x_min, y_min, x_max, y_max], outline='red', width=3)

resized_image.show()  # Display the resized image with adjusted bounding box