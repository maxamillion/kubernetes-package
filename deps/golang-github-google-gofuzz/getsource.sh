#!/bin/sh

rm gofuzz-*.tar.gz

wget https://github.com/google/gofuzz/archive/$1/gofuzz-${1:0:8}.tar.gz

#put the git hash in there
sed -i -e "s/%global commit\([[:space:]]\+\)[[:xdigit:]]\{40\}/%global commit\1$1/" golang-github-google-gofuzz.spec

#increment the version number
VAL=`sed -n -e "s/Release:[[:space:]]\+[[:digit:]]*.\([[:digit:]]*\).git.*/\1/p" golang-github-google-gofuzz.spec`
VAL=$((VAL + 1))
sed -i -e "s/\(Release:[[:space:]]\+[[:digit:]]*.\)\([[:digit:]]*\)\(.git\)/\1${VAL}\3/" golang-github-google-gofuzz.spec

sha256sum *.tar.gz *.spec > sources
