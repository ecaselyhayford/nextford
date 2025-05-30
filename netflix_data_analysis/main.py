# Import necessary libraries
from collections import Counter
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from unzip_file import unzip_and_rename

# Unzip the dataset and rename the file
unzip_and_rename("netflix_data.zip")


df = pd.read_csv("Netflix_shows_movies.csv")

# Data Exploration to check initial missing data
print("\n Data Info Summary:")
info_table = pd.DataFrame({
    "Column": df.columns,
    "Non-Null Count": df.notnull().sum(),
    "Missing Values Count": df.isnull().sum(),
})
print(tabulate(info_table, headers='keys', tablefmt='fancy_grid'))


# Data Cleaning - Handle missing values

# Fill missing values depending on column context
df['director'] = df['director'].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["date_added"] = df["date_added"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")


# Statistical Summary for selected columns
print("\n Statistical Summary (Selected Columns):")
summary = df[['type', 'rating', 'country']].describe(include='all').transpose()
print(tabulate(summary, headers='keys', tablefmt='fancy_grid'))

# Top 5 genres
print("\n Top 5 Most Frequent Genres:")
top_genres = df['listed_in'].value_counts().head().reset_index()
top_genres.columns = ['Genre', 'Count']
print(tabulate(top_genres, headers='keys', tablefmt='fancy_grid'))

# Top 5 directors
print("\n Top 5 Directors by Number of Shows/Movies:")
top_directors = df['director'].value_counts().head().reset_index()
top_directors.columns = ['Director', 'Count']
print(tabulate(top_directors, headers='keys', tablefmt='fancy_grid'))

# Top 5 countries
print("\n Top 5 Countries by Number of Shows/Movies:")
top_countries = df['country'].value_counts().head().reset_index()
top_countries.columns = ['Country', 'Count']
print(tabulate(top_countries, headers='keys', tablefmt='fancy_grid'))

# Duplicate rows
print("\n Number of Duplicate Rows:")
print(f"{df.duplicated().sum()} duplicate rows found.")

# Type distribution
print("\n Content Type Distribution (Movies vs TV Shows):")
type_dist = df['type'].value_counts().reset_index()
type_dist.columns = ['Type', 'Count']
print(tabulate(type_dist, headers='keys', tablefmt='fancy_grid'))


# Visualizations

# Flatten all genres into a single list
genres = df["listed_in"].dropna().str.split(", ")
flat_genres = [genre for sublist in genres for genre in sublist]
genre_counts = Counter(flat_genres)

# Convert to DataFrame for plotting
genre_df = pd.DataFrame(genre_counts.items(), columns=["Genre", "Count"]).sort_values(
    by="Count", ascending=False
)

# Plot: Most watched genres
plt.figure(figsize=(10, 6))
sns.barplot(x="Count", y="Genre", data=genre_df.head(
    10), hue="Genre", palette="coolwarm")
plt.title("Top 10 Most Watched Genres on Netflix")
plt.xlabel("Number of Shows/Movies")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig("top_genres.png")
# plt.show() # Enable this line to display the plot

# Rating distribution
plt.figure(figsize=(10, 5))
sns.countplot(
    y="rating", data=df, order=df["rating"].value_counts().index, hue="rating", palette="viridis"
)
plt.title("Distribution of Ratings")
plt.xlabel("Count")
plt.ylabel("Rating")
plt.tight_layout()
plt.savefig("rating_distribution.png")
# plt.show()  # Enable this line to display the plot
