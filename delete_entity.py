import sys
from datetime import datetime
from google.cloud import datastore

n = 500

def main():
    entity = sys.argv[1]
    start = datetime.now()

    print("CLEANUP entity {}".format(entity))
    client = datastore.Client(project='PROJECT-ID')
    query = client.query(kind=entity)
    query.keys_only()
    results = list(query.fetch())
    print("found {} entities".format(len(results)))

    keys = [item.key for item in results]
    chunks = [keys[i * n:(i + 1) * n] for i in range((len(keys) + n - 1) // n)]
    for chunk in chunks:
        client.delete_multi(chunk)

    stop = datetime.now()
    print("CLEANUP done - elapsed {}".format(stop - start))

if __name__ == "__main__":
    main()






