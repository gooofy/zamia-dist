#!/bin/bash

VERSION=0.5.7
PKGNAME=python-num2words
GITNAME=num2words
export DEBFULLNAME="Guenter Bartsch"

./clean.sh

cp -r ${GITNAME} ${PKGNAME}-${VERSION}
pushd ${PKGNAME}-${VERSION}
rm -rf .git

cp -r ../debian .

# dh_make -c lgpl3 -e 'guenter@zamia.org' --python --createorig
debuild -b -uc -us

popd

