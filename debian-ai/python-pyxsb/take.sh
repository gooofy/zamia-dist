#!/bin/bash

REPO=${HOME}/repo/ai/debian/stretch/amd64

rm -f ${REPO}/python*-pyxsb*.deb

cp python*-pyxsb*.deb ${REPO}

pushd ${REPO}
./update.sh
popd

