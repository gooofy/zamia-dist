#!/bin/bash

VERSION=3.8
PKGNAME=xsb
export DEBFULLNAME="Guenter Bartsch"

./clean.sh

tar xfvz ${PKGNAME}-${VERSION}.tar.gz

pushd ${PKGNAME}-${VERSION}

cp -r ../debian .

# dh_make -c mit -e 'guenter@zamia.org' --python --createorig
debuild -b -uc -us

popd

