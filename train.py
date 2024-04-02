from model import create_model
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical


def load_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255
    x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255
    y_train = to_categorical(y_train, 10)
    y_test = to_categorical(y_test, 10)
    return x_train, y_train, x_test, y_test


def train_model(model, x_train, y_train, x_test, y_test):
    model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=5, batch_size=128)


if __name__ == "__main__":
    x_train, y_train, x_test, y_test = load_data()
    model = create_model()
    train_model(model, x_train, y_train, x_test, y_test)
    model.save('mnist_cnn.h5')
