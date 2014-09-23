#!/bin/sh

# simple script to build and push to gh-pages
# designed to be run from master

# make the docs
make html

# copy to other repo (on the gh-pages branch)
cp -R build/html/ ../gh-pages-version/

cd ../gh-pages-version
git add * # in case there are new files added
git commit -a
git push
