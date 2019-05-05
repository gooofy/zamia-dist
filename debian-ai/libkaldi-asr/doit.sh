#!/bin/bash

VERSION="5.4.248"
GITNAME=kaldi
PKGNAME=libkaldi-asr
export DEBFULLNAME="Guenter Bartsch"

./clean.sh

# pushd ${GITNAME}
# make clean
# make README.md
# popd

cp -r ${GITNAME} ${PKGNAME}-${VERSION}
pushd ${PKGNAME}-${VERSION}
rm -rf .git

cp -r ../debian .
# cp ../linux_atlas.mk src/makefiles/

# dh_make -c lgpl3 -e 'guenter@zamia.org' --python --createorig
debuild -b -uc -us

popd

