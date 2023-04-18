import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt


f = tf.keras.datasets.fashion_mnist

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

print(x_train.shape)


model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(128, (3,3),activation="relu",input_shape=(28,28,1)),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.MaxPool2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3,3), activation="relu"),
    tf.keras.layers.MaxPool2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256,activation="relu"),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(10,activation="softmax"),
])

print(model.summary())


model.compile(optimizer="adam",loss=tf.keras.losses.SparseCategoricalCrossentropy(), metrics=["accuracy"])

model.fit(x_train, y_train, epochs=5)

test_loss, test_acc = model.evaluate(x_test,  y_test, verbose=2)

print('\nTest accuracy:', test_acc, "\nTest loss:",test_loss)

