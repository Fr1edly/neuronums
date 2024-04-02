import numpy as np
import os
from tensorflow.keras.models import load_model
from PIL import Image

def predict_images_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):  # Проверяем, что файл является PNG изображением
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)
            # Выполните предобработку изображения, если это необходимо
            # Выполните предсказание для изображения
            prediction = predict(image)  # Убедитесь, что функция predict() соответствующим образом определена
            print(f"Predicted for {filename}: {prediction}")

def load_and_prepare_image(image_path):
    img = Image.open(image_path).convert('L')  # Конвертация в черно-белое изображение
    img = img.resize((28, 28))  # Изменение размера изображения
    img_array = np.array(img)
    img_array = img_array.reshape(1, 28, 28, 1)  # Добавление размерности пакета
    img_array = img_array.astype('float32') / 255  # Нормализация
    return img_array

def predict(model_path, image_path):
    model = load_model(model_path)
    img_array = load_and_prepare_image(image_path)
    prediction = model.predict(img_array)
    return np.argmax(prediction, axis=1)[0]

if __name__ == "__main__":
    image_path = 'path_to_your_image.png'
    prediction = predict('mnist_cnn.h5', image_path)
    print(f"Predicted digit: {prediction}")
