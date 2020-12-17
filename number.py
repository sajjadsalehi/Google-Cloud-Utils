from google.cloud import datastore
import random
from datetime import datetime
import sys

TYPE = sys.argv[1] if len(sys.argv) > 1 else 'Task'
status = sys.argv[2] if len(sys.argv) > 2 else None

client = datastore.Client()
query = client.query(kind=TYPE)
if status is not None:
    query.add_filter('status', '=', status)
results = list(query.fetch())
print(len(results))