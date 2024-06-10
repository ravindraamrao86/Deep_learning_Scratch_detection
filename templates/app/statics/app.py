from flask import Flask, request, render_template
import os
from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img
import numpy as np

app = Flask(__name__)
model = load_model('model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join('uploads', filename)
        file.save(filepath)
        
        img = load_img(filepath, target_size=(128, 128))
        img = img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = img / 255.0
        
        prediction = model.predict(img)
        classes = ['scratch', 'dent', 'hole']
        predicted_class = classes[np.argmax(prediction)]
        
        return render_template('predict.html', prediction=predicted_class, image=filepath)

if __name__ == "__main__":
    app.run(debug=True)
