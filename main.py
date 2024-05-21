import argparse
import os
from predict import predict_images_in_folder
from train import train_model, load_data
from evaluate import evaluate_model
from model import create_model
# Импортируйте необходимые модули для обучения, предсказания и т.д.
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
def main():
    parser = argparse.ArgumentParser(description="Run neural network operations.")
    parser.add_argument('--mode', type=str, help='Mode of operation: train, predict, or run', required=True)
    args = parser.parse_args()

    if args.mode == 'train':
        x_train, y_train, x_test, y_test = load_data()
        model = create_model()
        train_model(model, x_train, y_train, x_test, y_test)
        model.save('./model/mnist_cnn.h5')
        pass
    elif args.mode == 'eval':
        evaluate_model('model/mnist_cnn.h5')
        pass
    elif args.mode == 'predict':
        folder_path = './draws'
        model_path = './model/mnist_cnn.h5'
        predict_images_in_folder(model_path, folder_path)
        pass
    elif args.mode == 'run':
        # Вызов функции обычного запуска из соответствующего модуля
        pass
    else:
        print("Invalid mode or missing arguments")

if __name__ == "__main__":
    main()
