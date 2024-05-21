import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model

def get_activations(model, model_inputs, layer_name=None):
    # Создаем модель, которая будет возвращать активации для конкретного слоя
    if layer_name is None:
        layers = [layer.output for layer in model.layers]
    else:
        layers = [layer.output for layer in model.layers if layer.name == layer_name]

    activation_model = Model(inputs=model.inputs, outputs=layers)
    activations = activation_model.predict(model_inputs)
    return activations

def display_activations(activations, col_size, row_size, layer_index):
    activation = activations[layer_index]
    activation_index = 0
    fig, ax = plt.subplots(row_size, col_size, figsize=(row_size*2.5, col_size*1.5))
    for row in range(row_size):
        for col in range(col_size):
            if activation_index < activation.shape[-1]:
                ax[row][col].imshow(activation[0, :, :, activation_index], cmap='gray')
                activation_index += 1
            ax[row][col].axis('off')

def load_and_prepare_image(image_path):
    img = image.load_img(image_path, target_size=(28, 28), color_mode='grayscale')
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype('float32') / 255
    return img_array

def display_images(image_path1, image_path2):
    img_array1 = load_and_prepare_image(image_path1)
    img_array2 = load_and_prepare_image(image_path2)

    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    axes[0].imshow(img_array1[0, :, :, 0], cmap='gray')
    axes[0].set_title('Image 1')
    axes[0].axis('off')

    axes[1].imshow(img_array2[0, :, :, 0], cmap='gray')
    axes[1].set_title('Image 2')
    axes[1].axis('off')

    plt.show()

# Загрузка модели
model = load_model('./model/mnist_cnn.h5')

# Загрузка и подготовка изображений
img_path1 = './draws/2.png'
img_path2 = './draws/4.png'
img1 = image.load_img(img_path1, target_size=(28, 28), color_mode='grayscale')
img2 = image.load_img(img_path2, target_size=(28, 28), color_mode='grayscale')
img_tensor1 = image.img_to_array(img1)
img_tensor2 = image.img_to_array(img2)
img_tensor1 = np.expand_dims(img_tensor1, axis=0)
img_tensor2 = np.expand_dims(img_tensor2, axis=0)
img_tensor1 /= 255.
img_tensor2 /= 255.

# Получение активаций
activations = get_activations(model, [img_tensor1, img_tensor2])
display_images(img_path1, img_path2)
# Визуализация активаций конкретного слоя
# Указываем индекс интересующего слоя и размер сетки для отображения
display_activations(activations, col_size=8, row_size=4, layer_index=0)

plt.show()
