#!/bin/bash

while IFS= read -r line || [[ -n "$line" ]]; do
    factors=$(factor "$line")
    echo "$line=$factors"
done < "tests/test00"

