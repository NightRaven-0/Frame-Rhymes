from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from Utils.image_caption import generate_caption
from Utils.generate_poem import generate_poem

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return '''
        <h1>Frame Rhymes API</h1>
        <p>Use the <code>/upload</code> endpoint to POST an image and mood.</p>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="image" required><br><br>
            <input type="text" name="mood" placeholder="Enter mood (e.g. calm, sad, happy)">
            <input type="submit" value="Upload">
        </form>
    '''


@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({"error": "No image part"}), 400

    image_file = request.files['image']
    mood = request.form.get('mood', 'calm')

    if image_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    caption = generate_caption(image_file)
    poem = generate_poem(caption, mood)

    return jsonify({
        "caption": caption,
        "filename": image_file.filename,
        "message": "Image uploaded successfully",
        "poem": poem
    })

if __name__ == "__main__":
    app.run(debug=True)
