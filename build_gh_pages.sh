#!/bin/sh

# simple script to build and push to gh-pages
# designed to be run from master

# make the docs
make html

git checkout gh-pages

cp -R build/html/ ./
git add * # not sure this works...
git commit -a
git push origin gh-pages
git push upstream gh-pages
git checkout master
