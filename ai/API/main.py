from fastapi import FastAPI, UploadFile, File
from typing import List
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import io

app = FastAPI()

# 모델 로드
model1 = models.resnet50(num_classes=3)
model2 = models.efficientnet_b2(num_classes=3)
# 모델 가중치 파일 로드
device = torch.device('cpu')

model1.load_state_dict(torch.load('normal_classification_64epoch.pth', map_location=device))
model1.eval()

model2.load_state_dict(torch.load('0826_09_1epoch.pth', map_location=device))
model2.eval()


# 이미지 전처리 함수
def preprocess_image1(image):
    transform = transforms.Compose([
        transforms.Resize(300),
        transforms.RandomResizedCrop(256),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0)


def preprocess_image2(image):
    transform = transforms.Compose([
        transforms.Resize((370, 370)),  # 이미지를 충분히 크게 리사이즈
        transforms.CenterCrop(260),  # 중앙 부분을 224x224 크기로 자름
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0)


# 이미지 업로드와 추론을 처리하는 엔드포인트
@app.post("/predict/")
async def predict(file: UploadFile):
    image = Image.open(io.BytesIO(file.file.read()))

    preprocessed_image1 = preprocess_image1(image)
    with torch.no_grad():
        outputs1 = model1(preprocessed_image1)

    probabilities1 = torch.nn.functional.softmax(outputs1[0], dim=0)
    predicted_class1 = torch.argmax(probabilities1).item()

    # 클래스 인덱스에 따른 클래스 이름 설정
    class_names = ['bad', 'good', 'normal']

    if class_names[predicted_class1] != 'good':
        preprocessed_image2 = preprocess_image2(image)

        with torch.no_grad():
            outputs2 = model2(preprocessed_image2)

        predicted_class2 = torch.argmax(outputs2).item()
        probabilities2= torch.nn.functional.softmax(outputs2[0], dim=0)
        class_names2 = ["class1", "class2", "class3"]
        predicted_class2 = class_names2[predicted_class2]

        return {'상태': class_names[predicted_class1], "predicted_class": predicted_class2, 'prob': probabilities2.tolist()}

    else:

        return {'상태': class_names[predicted_class1]}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)