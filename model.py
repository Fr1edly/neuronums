from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense, Conv2D, Flatten, MaxPooling2D, concatenate
from tensorflow.keras.models import Model

def create_model():
    input_shape = (28, 28, 1)

    input_img1 = Input(shape=input_shape)
    input_img2 = Input(shape=input_shape)

    merged = concatenate([input_img1, input_img2],axis=1)

    img = Conv2D(32, (3, 3), activation='relu')(merged)
    img = MaxPooling2D((2, 2))(img)
    img = Flatten()(img)
    '''processed_img1 = Conv2D(32, (3, 3), activation='relu')(input_img1)
    processed_img1 = MaxPooling2D((2, 2))(processed_img1)
    processed_img1 = Flatten()(processed_img1)

    processed_img2 = Conv2D(32, (3, 3), activation='relu')(input_img2)
    processed_img2 = MaxPooling2D((2, 2))(processed_img2)
    processed_img2 = Flatten()(processed_img2)'''

    prediction = Dense(100, activation='softmax')(img)

    model = Model(inputs=[input_img1, input_img2], outputs=prediction)

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model
