
# Netflix Shows and Movies Dataset Analysis

This project analyzes a dataset of Netflix shows and movies. It includes data preparation, cleaning, exploration, visualization using Python, and a basic integration into R for displaying one of the generated charts.

---

## Dataset

The dataset should be a `.zip` file containing a `.csv` file of Netflix data. After unzipping, the CSV will be renamed to `Netflix_shows_movies.csv`.

---

## Features Implemented

-  Unzipping and renaming the dataset
-  Handling missing data
-  Data exploration with statistical summaries
-  Visualizations using `matplotlib` and `seaborn`
-  Integration of a visualization chart into R

---

##  Setup Instructions

### 1.  Clone the Project

```bash
visit to clone the repo:  https://github.com/ecaselyhayford/nextford/tree/master/netflix_data_analysis
cd netflix_data_analysis
```

### 2.  Install Python Dependencies

Ensure you have Python 3.x installed. Then install the required packages:

```bash
pip install pandas matplotlib seaborn tabulate
```

---

##  How to Run

###  Run Python Script

Make sure your dataset zip file is in the project folder. Then run:

```bash
python main.py
```

The script will:
- Unzip and rename the dataset
- Clean and explore the data
- Display structured outputs in the terminal
- Generate visualizations and save them as PNG files

---

##  Visualizations

The script generates charts such as:
- Top 10 Most Watched Genres
- Distribution of Ratings

Charts are saved in the working directory as PNG files like `top_genres.png`.

---

##  Integration into R

To display one of the Python-generated charts in R:

###  Required R Packages

```r
install.packages("png")
install.packages("grid")
```

###  Display Image in R

```r
library(png)
library(grid)

img <- readPNG("top_genres.png")
grid.raster(img)
```
