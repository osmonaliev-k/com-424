#!/bin/bash
if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

directory=$1
empty_files=$(find "$directory" -type f -empty)

if [ -z "$empty_files" ]; then
    echo "No empty files found."
else
    echo "Deleting empty files:"
    echo "$empty_files"
    rm $empty_files
fi
