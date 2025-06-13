from tensorflow import keras
from keras import layers, Input
import numpy as np
from tabulate import tabulate

# Load the Fashion MNIST dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()

# Normalize pixel values to [0,1]
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Reshape to include channel dimension (batch, height, width, channels)
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

# Define the CNN model with six layers, using an Input layer first
input_shape = (28, 28, 1)
model = keras.Sequential(
    [
        # Input layer specifying shape
        Input(shape=input_shape),
        # 1) First convolutional layer
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        # 2) First pooling layer
        layers.MaxPooling2D(pool_size=(2, 2)),
        # 3) Second convolutional layer
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        # 4) Second pooling layer
        layers.MaxPooling2D(pool_size=(2, 2)),
        # 5) Flattening to 1D
        layers.Flatten(),
        # 6) Dense softmax output layer for 10 classes
        layers.Dense(10, activation="softmax"),
    ]
)
model.summary()

# Compile the model with optimizer, loss, and metrics
model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(),
    optimizer=keras.optimizers.Adam(learning_rate=1e-3),
    metrics=[
        keras.metrics.SparseCategoricalAccuracy(name="acc"),
    ],
)

# Train the model
callbacks = [
    keras.callbacks.ModelCheckpoint(filepath="model_at_epoch_{epoch}.keras"),
    keras.callbacks.EarlyStopping(monitor="val_loss", patience=2),
]
model.fit(
    x_train, y_train, epochs=5, batch_size=64, validation_split=0.1, callbacks=callbacks
)

# Evaluate on test set
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")
print(f"Test loss: {test_loss:.4f}")

# Make predictions on two images
results = []
for idx in [0, 1]:
    img = x_test[idx]
    img_input = np.expand_dims(img, 0)  # add batch dimension
    prediction = model.predict(img_input)
    predicted_class = np.argmax(prediction)
    results.append(
        {"Image Index": idx,
            "True Label": y_test[idx], "Predicted": predicted_class}
    )
print(tabulate(results, headers="keys", tablefmt="grid"))
