#!/bin/sh

rm go-dockerclient-*.tar.gz

wget https://github.com/fsouza/go-dockerclient/archive/$1/go-dockerclient-${1:0:8}.tar.gz

#put the git hash in there
sed -i -e "s/%global commit\([[:space:]]\+\)[[:xdigit:]]\{40\}/%global commit\1$1/" golang-github-fsouza-go-dockerclient.spec

#increment the version number
VAL=`sed -n -e "s/Release:[[:space:]]\+[[:digit:]]*.\([[:digit:]]*\).git.*/\1/p" golang-github-fsouza-go-dockerclient.spec`
VAL=$((VAL + 1))
sed -i -e "s/\(Release:[[:space:]]\+[[:digit:]]*.\)\([[:digit:]]*\)\(.git\)/\1${VAL}\3/" golang-github-fsouza-go-dockerclient.spec

sha256sum go-dockerclient-*.tar.gz golang-github-fsouza-go-dockerclient.spec > sources
