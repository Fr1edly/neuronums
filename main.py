import argparse
import os
from predict import predict_images_in_folder
# Импортируйте необходимые модули для обучения, предсказания и т.д.
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
def main():
    parser = argparse.ArgumentParser(description="Run neural network operations.")
    parser.add_argument('--mode', type=str, help='Mode of operation: train, predict, or run', required=True)
    args = parser.parse_args()

    if args.mode == 'train':
        # Вызов функции обучения из соответствующего модуля
        pass
    elif args.mode == 'eval':

        pass
    elif args.mode == 'predict':
        folder_path = './draws'
        predict_images_in_folder(folder_path)
        pass
    elif args.mode == 'run':
        # Вызов функции обычного запуска из соответствующего модуля
        pass
    else:
        print("Invalid mode or missing arguments")

if __name__ == "__main__":
    main()
