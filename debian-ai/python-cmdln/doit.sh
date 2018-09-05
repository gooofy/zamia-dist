#!/bin/bash

VERSION=1.3.1
PKGNAME=python-cmdln
export DEBFULLNAME="Guenter Bartsch"

./clean.sh

unzip cmdln-${VERSION}.zip

pushd cmdln-${VERSION}

# dh_make -c apache -e 'guenter@zamia.org' --python --createorig
cp -r ../debian .

debuild -b -uc -us

popd

