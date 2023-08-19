import io
import json
from fastapi import FastAPI, Request
import torchvision.transforms as transforms
from PIL import Image
from torchvision import models



app = FastAPI()

imagenet_class_index = json.load(open('image class/imagenet_class_index.json'))
model = models.densenet121(weights='IMAGENET1K_V1')
model.eval()


def transform_image(image_bytes):
    my_transforms = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)


with open("image class/OIP.jpg", 'rb') as f:
    image_bytes = f.read()
    tensor = transform_image(image_bytes=image_bytes)
    print(tensor)




def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return imagenet_class_index[predicted_idx]



@app.post('/predict')
def predict(file):
    img_bytes = await file.read()
    class_id, class_name = get_prediction(image_bytes=img_bytes)
    return {'class_id': class_id, 'class_name': class_name}


if __name__ == '__main__':
    app.run()