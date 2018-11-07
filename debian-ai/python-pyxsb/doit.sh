#!/bin/bash

VERSION=1.0.0
PKGNAME=python-pyxsb
GITNAME=py-xsb
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

# dh_make -c apache -e 'guenter@zamia.org' --python --createorig
cp -r ../debian .

debuild -b -uc -us

popd

