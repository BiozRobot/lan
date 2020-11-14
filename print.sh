#!/bin/bash
while read -r line; do
ip="$line"
torify ./PRET/pret.py $ip pjl -q -i ./commands.txt
done < "./ipprinter.txt"
