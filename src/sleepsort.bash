# Sleepsort
# Example usage: ./sleepsort.bash 1 4 4 2 5 3 4 6 2

#!/bin/bash
function sleepsort() {
    sleep "$1"
    echo "$1"
}

while [ -n "$1" ]
do
    sleepsort "$1" &
    shift
done
wait
