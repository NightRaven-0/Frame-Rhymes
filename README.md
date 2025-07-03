# 🖼️ Frame Rhymes

Frame Rhymes is an AI-powered web application that transforms your uploaded image into a poetic description based on a chosen mood. It combines image captioning and large language models to deliver creative and emotionally tuned poems.

---

## ✨ Features

- Upload an image (JPG/PNG).
- Choose a mood (e.g., calm, romantic, eerie, absurd, melancholic, etc.).
- Get a custom poem generated from the image and mood.
- View the generated caption and image.
- Download the poem as a `.txt` file.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

1. Clone your repo

- git clone https://github.com/your-username/frame-rhymes.git
- cd frame-rhymes


2. (Optional but Recommended) Create a Virtual Environment

- python -m venv venv
- source venv/bin/activate    # On Windows use: venv\Scripts\activate


3. Install Python Dependencies

- pip install -r requirements.txt


4. Download the Required Hugging Face Models

- cd backend
- python download_models.py
- cd ..


5. Start the App (Backend + Frontend)

- ./run.ps1  or double click the file run.ps1 in the root folder
- 📌 Wait for a few seconds until you see:

- Running on http://127.0.0.1:5000/
- That means the backend server is online.


6. Open the App
- No server hosting required! Just open this file manually in your browser:

- frontend/public/index.html

---

- You’re all set! 🎉 Upload an image, enter a mood, click Generate Poem, and enjoy your personalized verse

--- 