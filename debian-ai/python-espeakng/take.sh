#!/bin/bash

REPO=${HOME}/repo/ai/debian/stretch/amd64

rm -f ${REPO}/python*-espeakng*.deb

cp python*-espeakng*.deb ${REPO}

pushd ${REPO}
./update.sh
popd

