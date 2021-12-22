#!/bin/sh

# get parameter(IP)
IP="$1"

# reverse IP + spamhaus rbl dns
ADDR=`echo $IP | awk 'BEGIN{FS="."}{print $4"."$3"."$2"."$1".zen.spamhaus.org"}'`

# dig dns
DIG=$(dig +short $ADDR)

# check result after dig dns
NUM=${#DIG}

# run python
if [ "$NUM" != "0" ]; then
        /usr/bin/python3 spamhaus.py
fi
