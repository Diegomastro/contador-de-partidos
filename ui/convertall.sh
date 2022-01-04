#!/usr/bin/env bash

for file in *.ui
do
  #this newname var transforms   FILENAME.ui  into  ui_FILENAME.py
  newname="$(basename "$file")"
  newname="ui_${newname:0:(-3)}.py"
  pyuic5 "$file" -o "$newname"
  echo $newname
done