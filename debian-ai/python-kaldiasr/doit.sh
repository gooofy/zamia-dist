#!/bin/bash

VERSION=0.5.2
PKGNAME=python-kaldiasr
GITNAME=py-kaldi-asr
export DEBFULLNAME="Guenter Bartsch"

./clean.sh

cp -r ${GITNAME} ${PKGNAME}-${VERSION}
pushd ${PKGNAME}-${VERSION}
rm -rf .git

make clean

# dh_make -c apache -e 'guenter@zamia.org' --python --createorig

cp -r ../debian .

debuild -b -uc -us

