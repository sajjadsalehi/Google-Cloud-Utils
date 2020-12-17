from google.cloud import pubsub_v1
import json
import random
from datetime import datetime
import sys

project_id = "a2a-crmo-lab"
topic_id = "cron-topic"

MESSAGES_NUMBER = int(sys.argv[1]) if len(sys.argv) > 1 else 100
account_range = int(sys.argv[2]) if len(sys.argv) > 2 else 750
run_id = sys.argv[3] if len(sys.argv) > 3 else "1"
# Configure the batch to publish as soon as there is ten messages,
# one kilobyte of data, or one second has passed.
batch_settings = pubsub_v1.types.BatchSettings(
    max_messages=MESSAGES_NUMBER,  # default 100
    max_bytes=1024,  # default 1 MB
    max_latency=1,  # default 10 ms
)
publisher = pubsub_v1.PublisherClient(batch_settings)
topic_path = publisher.topic_path(project_id, topic_id)

# Resolve the publish future in a separate thread.
def callback(future):
    message_id = future.result()
    print(message_id)


for n in range(1, MESSAGES_NUMBER+1):
    data = '{"accountId": "%s", "timestamp": "%s", "runId" : "%s"}'%(str(random.randrange(1, account_range+1)), datetime.now(), run_id)
    # Data must be a bytestring
    data = data.encode("utf-8")
    future = publisher.publish(topic_path, data)
    # Non-blocking. Allow the publisher client to batch multiple messages.
    future.add_done_callback(callback)

print(f"Published messages with batch settings to {topic_path}.")