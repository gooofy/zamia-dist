#!/bin/bash

VERSION=2.0.11
PKGNAME=python-webrtcvad
GITNAME=py-webrtcvad
export DEBFULLNAME="Guenter Bartsch"

./clean.sh

cp -r ${GITNAME} ${PKGNAME}-${VERSION}
pushd ${PKGNAME}-${VERSION}
rm -rf .git

cp -r ../debian .

# dh_make -c mit -e 'guenter@zamia.org' --python --createorig
debuild -b -uc -us

popd

