#!/bin/bash
cd ..

git pull origin main

cd scripts
python add_to_readme.py

cd ..
git add .
msg="added todo list `date`"
if [ $# -eq 1 ]
    then msg="$1"
fi
git commit -m "$msg"

git push origin main
