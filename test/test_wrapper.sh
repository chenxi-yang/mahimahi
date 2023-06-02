#!/bin/bash
echo "Start wrapper test."
dir="."

test_name=$1
delay=10
qsize=120
trace="base_trace"
username=$(whoami)


sudo -u $username mm-delay $delay mm-link $trace --downlink-log "/log/down-${test_name}" --uplink-queue=droptail --uplink-queue-args "packets=${qsize}" --downlink-queue=droptail --downlink-queue-args "packets={qsize}" -- sh -c 
sudo -u `whoami` ${dir}/client $MAHIMAHI_BASE 1 0