from model import create_model
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

def load_data():
    # Загрузка данных MNIST
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # Подготовка данных для двух входов модели
    x_train = [x_train.reshape(-1, 28, 28, 1).astype('float32') / 255] * 2
    x_test = [x_test.reshape(-1, 28, 28, 1).astype('float32') / 255] * 2

    # Преобразование меток в one-hot кодировку
    y_train = to_categorical(y_train, 100)
    y_test = to_categorical(y_test, 100)

    return x_train, y_train, x_test, y_test

def train_model(model, x_train, y_train, x_test, y_test):
    # Обучение модели с двумя входами
    model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=5, batch_size=128)


if __name__ == "__main__":
    x_train, y_train, x_test, y_test = load_data()
    model = create_model()
    train_model(model, x_train, y_train, x_test, y_test)
    model.save('./model/mnist_cnn.h5')
