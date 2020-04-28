host="localhost:9092"
notification_topic="EventsTopic"
topics=`kafka-topics --list --zookeeper localhost:2181`
count=`echo $topics | grep -ic  $notification_topic`
if [ $count -eq 0 ]
then
  exec kafka-topics --create --bootstrap-server $host --replication-factor 1 --partitions 1 --topic $notification_topic
fi
