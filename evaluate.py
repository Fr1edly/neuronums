from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

def load_data():
    (_, _), (x_test, y_test) = mnist.load_data()
    x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255
    y_test = to_categorical(y_test, 10)
    return x_test, y_test

def evaluate_model(model_path):
    model = load_model(model_path)
    x_test, y_test = load_data()
    loss, accuracy = model.evaluate(x_test, y_test)
    print(f"Loss: {loss}, Accuracy: {accuracy}")
