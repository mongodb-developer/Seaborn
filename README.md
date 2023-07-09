<img src="https://img.appsious.com/logo/seaborn.jpg" alt="Seaborn Logo" width="50%">

Installing Seaborn
Open a command-line interface on your computer.

Install Seaborn by running the following command:

Copy code
pip install seaborn
Configuring access to MongoDB Atlas Movies collection
Sign in to your MongoDB Atlas account at https://www.mongodb.com/cloud/atlas (or create an account if you don't have one).

Set up a new project or choose an existing project.

Create a new cluster or select an existing cluster.

In the cluster settings, locate the connection string by clicking on the "Connect" button.

Choose "Connect your application" to get the connection string specific to your cluster.

Copy the connection string.

Open your Python script or Jupyter Notebook.

Install the PyMongo library if you haven't already by running the following command:

Copy code
pip install pymongo
Import the necessary libraries in your Python script:

python
Copy code
from pymongo import MongoClient
import seaborn as sns
import matplotlib.pyplot as plt
Set up a connection to your MongoDB Atlas cluster using the connection string you copied earlier:

python
Copy code
# Replace the connection string with your MongoDB Atlas connection string
connection_string = "mongodb+srv://<username>:<password>@<cluster-address>/test?retryWrites=true&w=majority"
client = MongoClient(connection_string)
Access the "movies" collection in the "sample_mflix" database:

python
Copy code
# Replace the database and collection names as needed
db = client['sample_mflix']
collection = db['movies']
Query the data from the collection:

python
Copy code
# Retrieve the data from MongoDB
documents = collection.find({})
Convert the MongoDB documents to a pandas DataFrame:

python
Copy code
import pandas as pd

# Convert MongoDB documents to a pandas DataFrame
df = pd.DataFrame(list(documents))
Perform any necessary data cleaning and transformation on the DataFrame.

Use Seaborn to create visualizations based on the data in the DataFrame. For example, you can create a scatter plot as follows:

python
Copy code
# Use Seaborn to create visualizations
sns.scatterplot(data=df, x='year', y='imdb.rating')

# Customize the plot as desired
# For example, you can add labels, titles, change the color palette, etc.

# Show the plot
plt.show()
Customize the plot as desired, such as adding labels, titles, changing the color palette, etc.

Run your Python script or execute the code in your Jupyter Notebook to visualize the data from the MongoDB Atlas Movies collection using Seaborn.


