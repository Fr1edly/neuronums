from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D

def create_model():
    input_shape = (28, 28, 1)

    input_img1 = Input(shape=input_shape)
    input_img2 = Input(shape=input_shape)

    processed_img1 = Conv2D(32, (3, 3), activation='relu')(input_img1)
    processed_img1 = MaxPooling2D((2, 2))(processed_img1)
    processed_img1 = Flatten()(processed_img1)

    processed_img2 = Conv2D(32, (3, 3), activation='relu')(input_img2)
    processed_img2 = MaxPooling2D((2, 2))(processed_img2)
    processed_img2 = Flatten()(processed_img2)

    merged = concatenate([processed_img1, processed_img2])

    prediction = Dense(100, activation='softmax')(merged)

    model = Model(inputs=[input_img1, input_img2], outputs=prediction)
    '''
    model = Sequential([
        Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(10, activation='softmax')
    ])
    '''

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model
