#!/bin/bash

VERSION=0.2.5
PKGNAME=python-nltools
GITNAME=py-nltools
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

