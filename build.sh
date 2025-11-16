#!/bin/bash

rm -rf ./dist
rm -rf ./address_book.egg-info

clear

python3 -m build

bash ./run.sh