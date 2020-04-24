#!/bin/bash
#export JAVA_HOME=/usr/java/jdk1.7.0_71
#export KAFKA_HOME=/var/hdata/kafka_2.10-0.10.2.0
export KAFKA_HOME=/var/hdata/kafka_2.10-0.10.2.0
export JAVA_HOME=/usr/java/jdk1.7.0_71
#显示某个消费组的消费详情
$KAFKA_HOME/bin/kafka-consumer-groups.sh --new-consumer --bootstrap-server bigdataap01:9092,bigdataap02:9092,bigdataap03:9092 --group $1 --describe


