#!/bin/sh

wget https://github.com/GoogleCloudPlatform/kubernetes/archive/$1/kubernetes-${1:0:8}.tar.gz

#put the git hash in there
sed -i -e "s/%global commit\t\t[[:xdigit:]]\{40\}/%global commit\t\t$1/" kubernetes.spec

#increment the version number
VAL=`sed -n -e "s/Release:\t[[:digit:]]*.[[:digit:]]*.\([[:digit:]]*\).git.*/\1/p" kubernetes.spec`
VAL=$((VAL + 1))
sed -i -e "s/\(Release:\t[[:digit:]]*.[[:digit:]]*.\)\([[:digit:]]*\)\(.git\)/\1${VAL}\3/" kubernetes.spec
