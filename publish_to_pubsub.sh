for i in {1..100}
do
	gcloud pubsub topics publish cron-topic  --message="hello from sajjad $i"
	sleep 0.2
done
