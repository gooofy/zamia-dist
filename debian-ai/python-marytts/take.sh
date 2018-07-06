#!/bin/bash

REPO=${HOME}/repo/ai/debian/stretch/amd64

rm -f ${REPO}/python*-marytts*.deb

cp python*-marytts*.deb ${REPO}

pushd ${REPO}
./update.sh
popd

