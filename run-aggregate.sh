#!/bin/bash
while yes | tail -n 55 /var/log/apache2/error.log; ./aggregate-logs.py ./error.log; do
   sleep 60
done
