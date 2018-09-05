#!/bin/bash

REPO=${HOME}/repo/ai/debian/stretch/amd64

rm -f ${REPO}/python*-zamiaai*.deb

cp python*-zamiaai*.deb ${REPO}

pushd ${REPO}
./update.sh
popd

