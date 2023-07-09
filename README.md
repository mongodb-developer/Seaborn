<img src="https://img.appsious.com/logo/seaborn.jpg" alt="Seaborn Logo" width="50%">

Installing Seaborn
Open a command-line interface on your computer.

Install Seaborn by running the following command:
```
pip3 install seaborn
```
Configuring access to MongoDB Atlas Movies collection
Sign in to your MongoDB Atlas account at https://www.mongodb.com/cloud/atlas (or create an account if you don't have one).

Open your Python script or Jupyter Notebook.

Install the PyMongo library if you haven't already by running the following command:
```
pip3 install pymongo
```
Import the necessary libraries in your Python script:
```
from pymongo import MongoClient
import seaborn as sns
import matplotlib.pyplot as plt
```
Set up a connection to your MongoDB Atlas cluster using the connection string you copied earlier:
```
# Replace the connection string with your MongoDB Atlas connection string
```
connection_string = "mongodb+srv://<username>:<password>@<cluster-address>/test?retryWrites=true&w=majority"
client = MongoClient(connection_string)
```
Access the "movies" collection in the "sample_mflix" database:

# Replace the database and collection names as needed
```
db = client['sample_mflix']
collection = db['movies']
``
Query the data from the collection:
``
# Retrieve the data from MongoDB
documents = collection.find({})
``
Convert the MongoDB documents to a pandas DataFrame:
python
```
import pandas as pd
```
# Convert MongoDB documents to a pandas DataFrame
```
df = pd.DataFrame(list(documents))
```
Perform any necessary data cleaning and transformation on the DataFrame.

Use Seaborn to create visualizations based on the data in the DataFrame. For example, you can create a scatter plot as follows:

# Use Seaborn to create visualizations
```
sns.scatterplot(data=df, x='year', y='imdb.rating')
```
# Customize the plot as desired
# For example, you can add labels, titles, change the color palette, etc.
# Show the plot
```
plt.show()
```
Run your Python script or execute the code in your Jupyter Notebook to visualize the data from the MongoDB Atlas Movies collection using Seaborn.
