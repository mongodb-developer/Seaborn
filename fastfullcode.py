#this version pulls on the first 100 records runs much faster
from pymongo import MongoClient
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Connect to MongoDB Atlas
client = MongoClient('mongodb+srv://xxxx:xxxx@shared-demo.xhytd.mongodb.net/test')

# Access the "movies" collection
db = client['sample_mflix']
collection = db['movies']

# Query all documents from the collection
cursor = collection.find()

# Retrieve the first 100 documents from the cursor
documents = []
for i, document in enumerate(cursor):
    documents.append(document)
    if i >= 99:
        break

# Convert data to a Pandas DataFrame
df = pd.DataFrame(documents)

# Extract the 'rating' subfield from the 'imdb' field
df['imdb_rating'] = df['imdb'].apply(lambda x: x['rating'] if 'rating' in x else None)

# Data processing steps
df['year'] = df['year'].astype(str).str.extract(r'(\d+)').astype(float)

# Plotting
sns.scatterplot(data=df, x='year', y='imdb_rating')
plt.show()
