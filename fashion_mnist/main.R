install.packages("keras")
install.packages("tensorflow")

library(keras)
library(tibble)
library(knitr)

# 1. Load the Fashion MNIST dataset
fashion_mnist <- dataset_fashion_mnist()
x_train <- fashion_mnist$train$x
y_train <- fashion_mnist$train$y
x_test  <- fashion_mnist$test$x
y_test  <- fashion_mnist$test$y

# 2. Normalize pixel values to [0,1]
x_train <- x_train / 255
x_test  <- x_test  / 255

# 3. Reshape to include channel dimension (batch, height, width, channels)
# Note: array_reshape will fill by rows, so we specify dims explicitly
x_train <- array_reshape(x_train, c(nrow(x_train), 28, 28, 1))
x_test  <- array_reshape(x_test,  c(nrow(x_test),  28, 28, 1))

# 4. Define the CNN model with six layers, starting with an Input layer
model <- keras_model_sequential() %>%
  # Input layer specifying shape
  layer_input(shape = c(28, 28, 1)) %>%
  # 1) First convolutional layer
  layer_conv_2d(filters = 32, kernel_size = c(3, 3), activation = "relu") %>%
  # 2) First pooling layer
  layer_max_pooling_2d(pool_size = c(2, 2)) %>%
  # 3) Second convolutional layer
  layer_conv_2d(filters = 64, kernel_size = c(3, 3), activation = "relu") %>%
  # 4) Second pooling layer
  layer_max_pooling_2d(pool_size = c(2, 2)) %>%
  # 5) Flatten to 1D
  layer_flatten() %>%
  # 6) Dense softmax output layer for 10 classes
  layer_dense(units = 10, activation = "softmax")

# Show model summary
model %>% summary()

# 5. Compile the model with optimizer, loss, and metrics
model %>% compile(
  loss      = "sparse_categorical_crossentropy",
  optimizer = optimizer_adam(learning_rate = 1e-3),
  metrics   = c("sparse_categorical_accuracy")
)

# 6. Set up callbacks: checkpointing and early stopping
callbacks <- list(
  callback_model_checkpoint(
    filepath = "model_at_epoch_{epoch}.h5",
    save_best_only = FALSE
  ),
  callback_early_stopping(
    monitor = "val_loss",
    patience = 2,
    restore_best_weights = TRUE
  )
)

# 7. Train the model
history <- model %>% fit(
  x_train, y_train,
  epochs          = 5,
  batch_size      = 64,
  validation_split = 0.1,
  callbacks       = callbacks
)

# 8. Evaluate on the test set
score <- model %>% evaluate(x_test, y_test, verbose = 0)
cat(sprintf("Test loss: %.4f\n", score["loss"]))
cat(sprintf("Test accuracy: %.4f\n", score["sparse_categorical_accuracy"]))

# 9. Make predictions on two images and tabulate results
results <- tibble(
  `Image Index` = integer(),
  `True Label`  = integer(),
  `Predicted`   = integer()
)

for (idx in c(1, 2)) {  # R is 1-based
  img       <- x_test[idx,,, , drop = FALSE]  # keep dims
  preds     <- model %>% predict(img)
  pred_class <- which.max(preds) - 1          # zero-based labels
  results <- add_row(
    results,
    `Image Index` = idx - 1,  # match Python’s 0-based indexing
    `True Label`  = y_test[idx],
    `Predicted`   = pred_class
  )
}

# Display as a grid-style table
kable(results, format = "markdown", row.names = FALSE)
