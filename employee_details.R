# Set the working directory to where the zip file is located
setwd("Employee Profile")

# Define the zip file name
zip_file <- "employee_details.zip"

# Unzip the contents
unzip(zip_file, exdir = "unzipped_data")

# List the files to confirm the CSV is extracted
files <- list.files("unzipped_data", full.names = TRUE)
print("Files extracted:")
print(files)

# Read the CSV file
employee_data <- read.csv(files[1])

# Display the first few rows
print("Employee Details:")
print(employee_data)
