import numpy as np
import os
from tensorflow.keras.models import load_model
from PIL import Image

def load_and_prepare_image(image_path):
    img = Image.open(image_path).convert('L')  # Convert to grayscale
    img = img.resize((28, 28))  # Resize image
    img_array = np.array(img)
    img_array = img_array.reshape(1, 28, 28, 1)  # Add batch dimension
    img_array = img_array.astype('float32') / 255  # Normalize
    return img_array

def predict(model_path, image_path1, image_path2):
    model = load_model(model_path)
    img_array1 = load_and_prepare_image(image_path1)
    img_array2 = load_and_prepare_image(image_path2)
    prediction = model.predict([img_array1, img_array2])
    return np.argmax(prediction, axis=1)[0]

def predict_images_in_folder(model_path, folder_path):
    image_paths = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith(".png")]
    for image_path1 in image_paths:
        for image_path2 in image_paths:
            prediction = predict(model_path, image_path1, image_path2)
            print(f"Predicted for {os.path.basename(image_path1)} + {os.path.basename(image_path2)}: {prediction}")


if __name__ == "__main__":
    image_path = 'path_to_your_image.png'
    prediction = predict('mnist_cnn.h5', image_path)
    print(f"Predicted digit: {prediction}")
