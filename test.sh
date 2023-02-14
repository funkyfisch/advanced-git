#!/bin/bash

git stash
git add .
git checkout -b $1
git stash pop

