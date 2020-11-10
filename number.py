from google.cloud import datastore
import random
from datetime import datetime


client = datastore.Client()
query = client.query(kind='Task')
results = list(query.fetch())
print(len(results))