#!/bin/sh

rm *.tar.gz

wget https://github.com/tools/godep/archive/$1/godep-${1:0:8}.tar.gz

#put the git hash in there
sed -i -e "s/%global commit\([[:space:]]\+\)[[:xdigit:]]\{40\}/%global commit\1$1/" golang-github-tools-godep.spec

rpmdev-bumpspec --comment="Bump to upstream ${1}" --userstring="Eric Paris <eparis@redhat.com" golang-github-tools-godep.spec

sha256sum *.tar.gz *.spec > sources
