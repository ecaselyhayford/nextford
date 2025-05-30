# Load necessary libraries
# Install these packages if not already installed
if (!require("png")) install.packages("png", dependencies = TRUE)
if (!require("grid")) install.packages("grid", dependencies = TRUE)

# Load the libraries
library(png)
library(grid)

# Set working directory
setwd(".")

# Read the image generated from Python
image_path <- "top_genres.png"
img <- readPNG(image_path)

# Display the image
grid.raster(img)
