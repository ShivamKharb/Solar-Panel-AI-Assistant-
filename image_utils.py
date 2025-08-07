# image_utils.py

import torch
import torchvision.models as models
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image

# Define image transforms
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

def load_model(model_path):
    model = models.resnet18(weights=None)
    model.fc = nn.Linear(model.fc.in_features, 2)  # 2 classes
    model.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")))
    model.eval()
    return model

def classify_image(image_pil, model):
    try:
        if image_pil.mode != 'RGB':
            image_pil = image_pil.convert('RGB')

        input_tensor = preprocess(image_pil).unsqueeze(0)
        with torch.no_grad():
            output = model(input_tensor)
            _, predicted = torch.max(output, 1)

        labels = ["non-rooftop", "rooftop"]
        return labels[predicted.item()]

    except Exception as e:
        return f"Error: {str(e)}"
