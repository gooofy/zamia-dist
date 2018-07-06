#!/bin/bash

VERSION=0.1.5
PKGNAME=python-espeakng
GITNAME=py-espeak-ng
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

