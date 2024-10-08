# Notice: Repository Deprecation
This repository is deprecated and no longer actively maintained. It contains outdated code examples or practices that do not align with current MongoDB best practices. While the repository remains accessible for reference purposes, we strongly discourage its use in production environments.
Users should be aware that this repository will not receive any further updates, bug fixes, or security patches. This code may expose you to security vulnerabilities, compatibility issues with current MongoDB versions, and potential performance problems. Any implementation based on this repository is at the user's own risk.
For up-to-date resources, please refer to the [MongoDB Developer Center](https://mongodb.com/developer).


<img src="https://img.appsious.com/logo/seaborn.jpg" alt="Seaborn Logo" width="50%">

# Create a cool matlabplot of the sample movies data in Atlas using Seaborn!
Installing Seaborn
Open up the terminal

Install Seaborn by running the following command:
```
pip3 install seaborn
```
Configuring access to MongoDB Atlas Movies collection
Sign in to your MongoDB Atlas account at https://www.mongodb.com/cloud/atlas (or create an account if you don't have one).

Open your terminal or Jupyter Notebook.

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
```
Query the data from the collection:
```
# Retrieve the data from MongoDB
documents = collection.find({})
```
Convert the MongoDB documents to a pandas DataFrame:

```
import pandas as pd
```
# Convert MongoDB documents to a pandas DataFrame
```
df = pd.DataFrame(list(documents))
```
Perform any necessary data cleaning and transformation on the DataFrame.

Use Seaborn to create visualizations based on the data in the DataFrame. For example, you can create a scatter plot as follows:

```
sns.scatterplot(data=df, x='year', y='imdb.rating')
```

# Show the plot
```
plt.show()
```
Run your Python script or execute the code in your Jupyter Notebook to visualize the data from the MongoDB Atlas Movies collection using Seaborn.

[Seaborn Documentation](https://seaborn.pydata.org/)
