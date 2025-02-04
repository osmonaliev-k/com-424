#!/bin/bash
if [ $# -ne 2 ]; then
    echo "Usage: $0 <filename> <word>"
    exit 1
fi

filename=$1
word=$2
count=$(grep -o -i "$word" "$filename" | wc -l)

echo "The word '$word' appears $count times in the file '$filename'."
