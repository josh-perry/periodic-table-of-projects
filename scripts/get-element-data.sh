#!/bin/bash

if [ -z $GITHUB_USERTOKEN ]; then
  echo "GitHub user/token not supplied!"
  exit 1
fi

mkdir -p raw_data

searchUrl="https://api.github.com/search/repositories"

readarray elements < elements.txt

for element in "${elements[@]}"
do
  element=${element//$'\n'/}

  echo "Processing $element"
  curl -u $GITHUB_USERTOKEN "$searchUrl?q=${element}" -o "raw_data/${element}"
  sleep 1
done
