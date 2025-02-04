#!/bin/bash
current_time=$(date +"%H:%M")
work_end="18:00"
remaining_time=$(($(date -j -f "%H:%M" "$work_end" +%s) - $(date -j -f "%H:%M" "$current_time" +%s)))
hours=$((remaining_time / 3600))
minutes=$(((remaining_time % 3600) / 60))

echo "Current time: $current_time"
echo "Work day ends after $hours hours and $minutes minutes."
