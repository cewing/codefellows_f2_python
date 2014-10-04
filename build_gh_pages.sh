#!/bin/sh

# simple script to build and push to gh-pages
# designed to be run from master

# make sure this repo is updated in gitHub:
git commit -a

git push

# make the docs
make html

# copy to other repo (on the gh-pages branch)
cp -R build/html/ ../gh-pages-version/

# go to other clone and push the html
cd ../gh-pages-version
git add * # in case there are new files added
git commit -a
git push

# while we're at it, push the class repo too:
cd ../sea-f2-python-sept14/
git commit -a
git push
