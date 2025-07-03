from transformers import BlipProcessor, BlipForConditionalGeneration
import os

MODEL_NAME = "Salesforce/blip-image-captioning-base"
CACHE_DIR = "./hf_models"

os.makedirs(CACHE_DIR, exist_ok=True)

print("🔽 Downloading BLIP processor...")
BlipProcessor.from_pretrained(MODEL_NAME, cache_dir=CACHE_DIR)

print("🔽 Downloading BLIP model...")
BlipForConditionalGeneration.from_pretrained(MODEL_NAME, cache_dir=CACHE_DIR)

print("✅ All models downloaded to", CACHE_DIR)
