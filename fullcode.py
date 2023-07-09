#works with mongodb atlas sample movie data set "sample_mflix"

import sys
from pymongo import MongoClient
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Prevent multiple runs
if not hasattr(sys, 'called_from_seaborn_script'):
    sys.called_from_seaborn_script = True
else:
    sys.exit(0)

# Connect to MongoDB Atlas
connection_string = "mongodb+srv://xxxx:xxxx@shared-demo.xhytd.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(connection_string)

# Access the "movies" collection in the "sample_mflix" database
db = client['sample_mflix']
collection = db['movies']

# Retrieve the data from MongoDB
documents = collection.find({})

# Convert MongoDB documents to a pandas DataFrame
df = pd.DataFrame(list(documents))

# Print the first few rows of the DataFrame to inspect the column names and structure
print(df.head())

# Extract the IMDb rating from the "imdb" field
df['imdb.rating'] = df['imdb'].apply(lambda x: float(x.get('rating')) if x.get('rating') else float('NaN'))

# Clean the "year" column
df['year'] = df['year'].str.extract(r'(\d+)').astype(float)

# Use Seaborn to create visualizations
sns.scatterplot(data=df, x='year', y='imdb.rating')
# Customize the plot as desired
# For example, you can add labels, titles, change the color palette, etc.

# Show the plot
plt.show()
