#!/bin/bash

git stash
git add .
git checkout $1
git stash pop

