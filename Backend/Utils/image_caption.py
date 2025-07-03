from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import os

# Optional: force offline mode
os.environ["TRANSFORMERS_OFFLINE"] = "1"

# Load processor and model from local cache
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base", cache_dir="./hf_models")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base", cache_dir="./hf_models")

def generate_caption(image_path):
    image = Image.open(image_path).convert('RGB')
    
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        out = model.generate(**inputs)
    
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption
