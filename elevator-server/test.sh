#!/bin/sh

for floor in 3 -2 -9 9 4 18 102
do
    curl -X 'POST' "http://127.0.0.1:8000/floor/$floor" -H 'accept: application/json' -d '' | python3 -mjson.tool
done
