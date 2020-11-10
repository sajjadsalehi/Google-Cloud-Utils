
import sys
import random
from datetime import datetime
from google.cloud import datastore

n = 500

def main():
    total = sys.argv[1] if len(sys.argv) > 1 else 1000
    account_range = int(sys.argv[2]) if len(sys.argv) > 2 else 750

    print("CREATING {} task".format(total))
    start = datetime.now()

    client = datastore.Client(project='PROJECT-ID')

    tasks = []
    for i in range(total):
        task = datastore.Entity(key=client.key('Task'))
        task['accountId'] = format(random.randrange(1, account_range+1))
        task['timestamp'] = datetime.now()
        task['status'] = "toprocess"
        tasks.append(task)
    print("task generated".format(total))

    chunks = [tasks[i * n:(i + 1) * n] for i in range((len(tasks) + n - 1) // n)]
    for chunk in chunks:
        client.put_multi(chunk)

    stop = datetime.now()
    print("CREATING done - elapsed {}".format(stop - start))


if __name__ == "__main__":
    main()