#!/usr/bin/env bash

function rand(){
    min=$1
    max=$2
    random_number=$(($RANDOM+100000))
    ans=$(($random_number%($max-$min)+$min))
    return $ans
}

music_dir="$(cd "$(dirname "$0")"; pwd)"
cd "resource"
echo $(pwd)

songs=()
i=0

for song in $("ls")
do
    songs[$i]=$song
    i=$((i+1))
done

len=${#songs[*]}

while [[ true ]]; do
    rand 0 $len
    ans=$?
    play ${songs[$ans]}
done
