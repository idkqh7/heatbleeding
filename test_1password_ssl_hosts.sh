#!/bin/sh

SCRIPT_DIR=$(dirname $0)


python "$SCRIPT_DIR/get_1password_https_hosts.py" | while read h; do 
    result=$(python "$SCRIPT_DIR/ssltest.py" $h | tail -1 | grep WARNING)
    if [ -z "$result" ]; then
       result="OK"
    fi
    echo "$h: $result"
done
