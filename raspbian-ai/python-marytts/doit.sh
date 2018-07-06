#!/bin/bash

VERSION=0.1.4
PKGNAME=python-marytts
GITNAME=py-marytts
export DEBFULLNAME="Guenter Bartsch"

./clean.sh

pushd ${GITNAME}
make clean
make README.md
popd

cp -r ${GITNAME} ${PKGNAME}-${VERSION}
pushd ${PKGNAME}-${VERSION}
rm -rf .git
make clean README.md
cp -r ../debian .

# dh_make -c lgpl3 -e 'guenter@zamia.org' --python --createorig
debuild -b -uc -us

popd

