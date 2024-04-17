from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

def load_data():
    (_, _), (x_test, y_test) = mnist.load_data()
    x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255
    # Duplicate x_test for the two inputs and ensure y_test has the correct number of classes
    x_test_1 = x_test_2 = x_test
    y_test = to_categorical(y_test, 100)  # Assuming 10 classes for MNIST
    return x_test_1, x_test_2, y_test

def evaluate_model(model_path):
    model = load_model(model_path)
    x_test_1, x_test_2, y_test = load_data()
    # Provide both sets of test images to the model for evaluation
    loss, accuracy = model.evaluate([x_test_1, x_test_2], y_test)
    print(f"Loss: {loss}, Accuracy: {accuracy}")

